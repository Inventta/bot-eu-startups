import pandas as pd
from constants import CLEAN_FILE, FINAL_FILE

# Ler as 10 primeiras linhas do arquivo transformed_data.xlsx
data = pd.read_excel(f"../{FINAL_FILE}")

# Remover duplicatas com base na coluna "Organization Name"
data_limpo = data.drop_duplicates(subset="Organization Name", keep="first")

# Salvar os dados limpos em outro arquivo xlsx
data_limpo.to_excel(CLEAN_FILE, index=False)
