import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract_data_from_url(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print('Solicitação bem-sucedida. Analisando o HTML...')
            
            soup = BeautifulSoup(response.content, 'html.parser')
            listings = soup.find_all('div', class_='wpbdp-listing')
            
            data_list = []
            for listing in listings:
                title = listing.find('div', class_='listing-title').find('a').text.strip()
                path = listing.find('div', class_='listing-title').find('a')['href']
                
                data = {'Title': title, 'Path': path}
                data_list.append(data)
            
            return data_list
        else:
            print(f'Erro ao acessar a URL: {url}')
            return []
    except Exception as e:
        print(f'Erro ao processar a URL {url}: {e}')
        return []

def extract_info_from_site(url, title):
    try:
        print(f'Extraindo informações do site: {url}')
        
        response = requests.get(url)
        
        if response.status_code == 200:
            print('Solicitação bem-sucedida... Analisando o HTML...')
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            info_template = {
                'Name': title,
                'Category': '',
                'Business Description': '',
                'Long Business Description': '',
                'Based in': '',
                'Tags': '',
                'Total Funding': '',
                'Founded': '',
                'Website': '',
                'Company Status': ''
            }
            
            for key in info_template.keys():
                if key != 'Name':
                    info_template[key] = get_info(soup, key)
            
            print('Informações extraídas com sucesso.')
            
            return info_template
        else:
            print(f'Erro ao acessar a URL: {url}')
            return {key: '' for key in info_template.keys()}
    except Exception as e:
        print(f'Erro ao processar a URL {url}: {e}')
        return {key: '' for key in info_template.keys()}

def get_info(soup, label):
    try:
        element = soup.find('span', class_='field-label', text=label)
        if element:
            value = element.find_next_sibling('div', class_='value').text.strip()
            return value
        else:
            return ''
    except Exception as e:
        print(f'Erro ao extrair informação {label}: {e}')
        return ''

def transform_data(data):
    transformed_data = []
    for item in data:
        website = item.get("Website", "").split(" / ")[0]

        # Check if the URL starts with "http" or "www" and add "https://" if necessary
        if website.startswith("http"):
            website = website
        elif website.startswith("www"):
            website = f"https://{website}"
        else:
            website = f"https://www.{website}"

        # Remove trailing slashes from the URL
        website = website.rstrip("/")
    
        location = f"{item.get('Based in', '')}, {item.get('Category', '')}"

        foundation = item.get("Founded", "")

        if foundation != "N/D":
            foundation = f"{int(foundation)}-01-01"
        
        description = item.get("Business Description", "")

        if description is not None:
            description = description.replace("\n", "")

        item_transformed = {
            "Headquarters Location": location,
            "IPO Status": "",
            "Operating Status": item.get("Company Status", ""),
            "Last Funding Type": "",
            "Organization Name": item.get("Name", ""),
            "Organization Name URL": website,
            "Number of Funding Rounds": "",
            "Description": description,
            "Founded Date": foundation,
            "Founded Date Precision": "year",
            "Website": website,
            "Contact Email": "",
            "Industries": item.get("Tags", ""),
            "LinkedIn": "",
            "Industry Groups": item.get("Tags", ""),
            "Founders": ""
        }
        transformed_data.append(item_transformed)
    return transformed_data

def process_json_data(input_file_name, output_file_name):
    with open(input_file_name, 'r') as file:
        data = json.load(file)['data']
    transformed_data = transform_data(data)
    df = pd.DataFrame(transformed_data)
    df.to_excel(output_file_name, index=False)
    return transformed_data
