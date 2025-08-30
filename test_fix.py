#!/usr/bin/env python3
"""
Teste simples para verificar se o fix dos headers funcionou
"""

import requests
from bs4 import BeautifulSoup

def test_with_headers():
    """Testa o site com os novos headers"""
    url = "https://www.eu-startups.com/directory/conbaseai/"
    
    # Headers que adicionamos
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        print(f"🔍 Testando: {url}")
        response = requests.get(url, headers=headers, timeout=30)
        
        print(f"✅ Status: {response.status_code}")
        print(f"📏 Tamanho: {len(response.content)} bytes")
        
        if response.status_code == 200:
            print("🎉 SUCESSO! Headers funcionaram!")
            
            # Testar se consegue extrair dados
            soup = BeautifulSoup(response.content, 'html.parser')
            field_labels = soup.find_all('span', class_='field-label')
            print(f"📋 Encontrados {len(field_labels)} field-labels")
            
            if field_labels:
                print("✅ Estrutura HTML encontrada!")
                return True
            else:
                print("⚠️  Estrutura HTML não encontrada")
                return False
        else:
            print(f"❌ Ainda bloqueado - Status: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Testando fix dos headers...")
    success = test_with_headers()
    
    if success:
        print("\n🎯 Fix funcionou! Pode executar o script principal.")
    else:
        print("\n⚠️  Fix não funcionou. Pode precisar de outras soluções.")
