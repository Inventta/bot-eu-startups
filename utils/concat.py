import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from constants import BASE_LABI, CLEAN_FILE, CONCATENATED_FILE

def concatenate_excel_files(file1, file2):
    # Check if files exist
    if not os.path.exists(file1):
        print(f"ERRO: Arquivo {file1} não encontrado!")
        print(f"Por favor, coloque o arquivo {file1} na pasta raiz do projeto.")
        return False
    
    if not os.path.exists(file2):
        print(f"ERRO: Arquivo {file2} não encontrado!")
        print(f"Execute primeiro o script clean.py para gerar o arquivo {file2}.")
        return False
    
    # Read the excel files
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)
    
    # Concatenate the DataFrames
    concatenated_df = pd.concat([df1, df2], ignore_index=True)
    
    # Save the concatenated DataFrame to a new excel file
    concatenated_df.to_excel(CONCATENATED_FILE, index=False)
    print(f"Files {file1} and {file2} successfully concatenated in {CONCATENATED_FILE}.")
    return True


if __name__ == "__main__":
    concatenate_excel_files(BASE_LABI, CLEAN_FILE)
