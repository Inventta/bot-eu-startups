#!/bin/bash

# Script para executar concat.py com nohup e salvar logs com timestamp
# Formato do arquivo: DDMMAAAA-HHMM_concat.log

# Obter timestamp no formato DDMMAAAA-HHMM
TIMESTAMP=$(date +"%d%m%Y-%H%M")
LOG_FILE="${TIMESTAMP}_concat.log"

echo "🔗 Iniciando execução do concat.py..."
echo "📝 Log será salvo em: $LOG_FILE"
echo "⏰ Timestamp: $TIMESTAMP"
echo ""

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Verificar se há processos do concat.py rodando
echo "🔍 Verificando processos existentes..."
EXISTING_PROCESSES=$(ps aux | grep concat.py | grep -v grep | wc -l)

if [ $EXISTING_PROCESSES -gt 0 ]; then
    echo "⚠️  Encontrados $EXISTING_PROCESSES processo(s) do concat.py rodando."
    echo "🛑 Parando processos existentes..."
    pkill -f concat.py
    sleep 2
    echo "✅ Processos parados."
else
    echo "✅ Nenhum processo do concat.py encontrado."
fi

# Executar concat.py com nohup
echo "▶️  Executando concat.py com nohup..."
nohup python utils/concat.py > "$LOG_FILE" 2>&1 &

# Obter o PID do processo
CONCAT_PID=$!
echo "📊 PID do processo: $CONCAT_PID"

# Aguardar um pouco para verificar se iniciou
sleep 2

# Verificar se o processo está rodando
if ps -p $CONCAT_PID > /dev/null; then
    echo "✅ Processo iniciado com sucesso!"
    echo "📋 Comandos úteis:"
    echo "   Ver logs em tempo real: tail -f $LOG_FILE"
    echo "   Verificar processo: ps aux | grep concat.py"
    echo "   Parar processo: kill $CONCAT_PID"
else
    echo "❌ Erro ao iniciar o processo!"
    echo "📄 Verifique o log: cat $LOG_FILE"
fi

echo ""
echo "🎯 Script concluído!"
