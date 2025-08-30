# Instruções para Execução do Projeto 🚀

Este guia irá ajudá-lo a configurar e rodar o projeto em sua máquina local.

## Pré-requisitos 📋

Antes de começar, certifique-se de ter Python 3 instalado em sua máquina.

## Configuração do Ambiente Virtual 🔧

Para evitar conflitos com o sistema, é recomendado usar um ambiente virtual. Execute os seguintes comandos:

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate  # No macOS/Linux
# ou
venv\Scripts\activate     # No Windows

# Instalar as bibliotecas necessárias
pip install beautifulsoup4 pandas requests openpyxl
```

**Nota:** Sempre ative o ambiente virtual antes de executar o projeto:
```bash
source venv/bin/activate
```

## Bibliotecas Utilizadas 📚

- **beautifulsoup4**: Para web scraping e parsing HTML
- **pandas**: Para manipulação e análise de dados
- **requests**: Para fazer requisições HTTP
- **openpyxl**: Para leitura e escrita de arquivos Excel

## Execução do Projeto 📁

**IMPORTANTE:** Antes de executar os scripts, você precisa:

1. **Colocar o arquivo Excel base** na pasta raiz do projeto com o nome `base-labi.xlsx`
   - Este é o arquivo Excel antigo que será concatenado com os novos dados
   - O arquivo deve estar na pasta raiz (mesmo nível de `main.py`)

2. **Verificar se o ambiente virtual está ativo:**
   ```bash
   source venv/bin/activate
   ```

Após garantir que o arquivo `base-labi.xlsx` está na pasta raiz, execute os seguintes scripts na ordem indicada **a partir da pasta raiz do projeto**:

```bash
# Certifique-se de estar na pasta raiz do projeto

# Execute os scripts na ordem:
python main.py
python utils/clean.py
python utils/concat.py
python utils/refine.py
```

**Importante:** Sempre execute os scripts a partir da pasta raiz do projeto para que os imports funcionem corretamente.

## Desativação do Ambiente Virtual 🚪

Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual:
```bash
deactivate
```

## Para rodar em segundo plano (Instâncias/Servidores) 🖥️

**IMPORTANTE:** Use estes scripts quando quiser executar em segundo plano (continua rodando mesmo fechando o terminal).

### Preparar os scripts (uma vez só):
```bash
chmod +x run_main.sh run_clean.sh run_concat.sh run_refine.sh
```

### Executar na ordem (um por vez):
```bash
# 1. Coleta de dados
./run_main.sh

# 2. Limpeza dos dados (execute após o main terminar)
./run_clean.sh

# 3. Concatenação (execute após o clean terminar)
./run_concat.sh

# 4. Refinamento final (execute após o concat terminar)
./run_refine.sh
```

### Comandos úteis para acompanhar:

**Ver logs em tempo real:**
```bash
# Substitua [timestamp] pelo nome do arquivo gerado (ex: 30082025-1048_main.log)
tail -f [timestamp]_main.log
tail -f [timestamp]_clean.log
tail -f [timestamp]_concat.log
tail -f [timestamp]_refine.log
```

**Verificar se os processos estão rodando:**
```bash
ps aux | grep main.py
ps aux | grep clean.py
ps aux | grep concat.py
ps aux | grep refine.py
```

**Parar processos (se necessário):**
```bash
pkill -f main.py
pkill -f clean.py
pkill -f concat.py
pkill -f refine.py
```
