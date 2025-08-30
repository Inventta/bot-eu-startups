import json
import os
import time
from constants import PAGE_MAX, BACKUP_STEP_1_FILE_NAME, BACKUP_STEP_2_FILE_NAME, FINAL_FILE, BASE_URL
from services import extract_data_from_url, extract_info_from_site, process_json_data

all_data = []
all_data_backup = []

loop_max = PAGE_MAX + 1

if os.path.exists(BACKUP_STEP_1_FILE_NAME):
    with open(BACKUP_STEP_1_FILE_NAME, "r") as backup_file:
        data = json.load(backup_file)
        all_data = data.get("data", [])

# STEP 1
if not all_data:
    for page_number in range(1, loop_max):
        try:
            print(" ")
            print(f"Index atual: {page_number - 1} - Total de iterações: {loop_max - 1}")
            url_base = f"{BASE_URL}{page_number}"
            data_list = extract_data_from_url(url_base)
            all_data.extend(data_list)
            all_data_backup.extend(data_list)

            dados_pagina = {"page_number": page_number}
            all_data_backup.append(dados_pagina)

            with open(BACKUP_STEP_1_FILE_NAME, "w") as backup_file:
                json.dump({"data": all_data}, backup_file)
                backup_file.write("\n")
            
            # Delay para evitar rate limiting
            time.sleep(2)

        except Exception as e:
            print(f"Erro ao processar a página {page_number}: {e}")
            continue
    

dados = []

# STEP 2
for item in all_data:
    try:
        print(" ")
        print(f"Index atual: {all_data.index(item)} - Total de iterações: {len(all_data)}")

        if 'Path' in item and 'Title' in item:
            info = extract_info_from_site(item['Path'], item['Title'])
        else:
            print("Chave 'Path' ou 'Title' não encontrada no item.")

        if info:
            dados.append(info)

        # Delay para evitar rate limiting
        time.sleep(1)

    except Exception as e:
        print(f"Erro ao processar o item. {e}")
        continue

with open(BACKUP_STEP_2_FILE_NAME, "w") as json_file:
    json.dump({"data": dados}, json_file)

process_json_data(BACKUP_STEP_2_FILE_NAME, FINAL_FILE)
