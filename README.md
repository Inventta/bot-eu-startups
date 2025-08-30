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
