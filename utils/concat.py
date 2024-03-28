import pandas as pd
from constants import BASE_LABI, CLEAN_FILE, CONCATENATED_FILE

def concatenate_excel_files(file1, file2):
    # Read the excel files
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)
    
    # Concatenate the DataFrames
    concatenated_df = pd.concat([df1, df2], ignore_index=True)
    
    # Save the concatenated DataFrame to a new excel file
    concatenated_df.to_excel(CONCATENATED_FILE, index=False)
    print(f"Files {file1} and {file2} successfully concatenated in {CONCATENATED_FILE}.")


concatenate_excel_files(BASE_LABI, CLEAN_FILE)
