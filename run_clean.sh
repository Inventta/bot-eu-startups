#!/bin/bash

# Script para executar clean.py com nohup e salvar logs com timestamp
# Formato do arquivo: DDMMAAAA-HHMM_clean.log

# Obter timestamp no formato DDMMAAAA-HHMM
TIMESTAMP=$(date +"%d%m%Y-%H%M")
LOG_FILE="${TIMESTAMP}_clean.log"

echo "🧹 Iniciando execução do clean.py..."
echo "📝 Log será salvo em: $LOG_FILE"
echo "⏰ Timestamp: $TIMESTAMP"
echo ""

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Verificar se há processos do clean.py rodando
echo "🔍 Verificando processos existentes..."
EXISTING_PROCESSES=$(ps aux | grep clean.py | grep -v grep | wc -l)

if [ $EXISTING_PROCESSES -gt 0 ]; then
    echo "⚠️  Encontrados $EXISTING_PROCESSES processo(s) do clean.py rodando."
    echo "🛑 Parando processos existentes..."
    pkill -f clean.py
    sleep 2
    echo "✅ Processos parados."
else
    echo "✅ Nenhum processo do clean.py encontrado."
fi

# Executar clean.py com nohup
echo "▶️  Executando clean.py com nohup..."
nohup python utils/clean.py > "$LOG_FILE" 2>&1 &

# Obter o PID do processo
CLEAN_PID=$!
echo "📊 PID do processo: $CLEAN_PID"

# Aguardar um pouco para verificar se iniciou
sleep 2

# Verificar se o processo está rodando
if ps -p $CLEAN_PID > /dev/null; then
    echo "✅ Processo iniciado com sucesso!"
    echo "📋 Comandos úteis:"
    echo "   Ver logs em tempo real: tail -f $LOG_FILE"
    echo "   Verificar processo: ps aux | grep clean.py"
    echo "   Parar processo: kill $CLEAN_PID"
else
    echo "❌ Erro ao iniciar o processo!"
    echo "📄 Verifique o log: cat $LOG_FILE"
fi

echo ""
echo "🎯 Script concluído!"
