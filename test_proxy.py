#!/usr/bin/env python3
"""
Teste com diferentes proxies para contornar bloqueio da AWS
"""

import requests
from bs4 import BeautifulSoup
import time

def test_with_proxy(proxy_url=None):
    """Testa o site com proxy"""
    url = "https://www.eu-startups.com/directory/conbaseai/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    proxies = None
    if proxy_url:
        proxies = {
            'http': proxy_url,
            'https': proxy_url
        }
        print(f"🔧 Usando proxy: {proxy_url}")
    
    try:
        print(f"🔍 Testando: {url}")
        response = requests.get(url, headers=headers, proxies=proxies, timeout=30)
        
        print(f"✅ Status: {response.status_code}")
        print(f"📏 Tamanho: {len(response.content)} bytes")
        
        if response.status_code == 200:
            print("🎉 SUCESSO! Proxy funcionou!")
            
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

def test_different_proxies():
    """Testa diferentes proxies"""
    print("🚀 Testando diferentes proxies...")
    
    # Lista de proxies públicos (pode não funcionar, mas vamos tentar)
    proxy_list = [
        None,  # Sem proxy primeiro
        "http://proxy.freemyip.com:8080",
        "http://proxy.zenrows.com:8001",
        "http://proxy.scrapingbee.com:8080",
        "http://proxy.brightdata.com:22225",
    ]
    
    for i, proxy in enumerate(proxy_list):
        print(f"\n{'='*50}")
        print(f"Teste {i+1}/{len(proxy_list)}")
        
        if test_with_proxy(proxy):
            print(f"🎯 Proxy funcionou: {proxy}")
            return proxy
        
        time.sleep(2)  # Delay entre testes
    
    return None

def test_alternative_headers():
    """Testa headers alternativos"""
    print("\n🔧 Testando headers alternativos...")
    
    url = "https://www.eu-startups.com/directory/conbaseai/"
    
    # Headers mais agressivos
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Cache-Control': 'max-age=0',
    }
    
    try:
        print(f"🔍 Testando com headers alternativos...")
        response = requests.get(url, headers=headers, timeout=30)
        
        print(f"✅ Status: {response.status_code}")
        
        if response.status_code == 200:
            print("🎉 Headers alternativos funcionaram!")
            return True
        else:
            print(f"❌ Ainda bloqueado")
            return False
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Iniciando testes de proxy...")
    
    # Teste 1: Headers alternativos
    if test_alternative_headers():
        print("\n🎯 Headers alternativos funcionaram!")
        exit(0)
    
    # Teste 2: Proxies
    working_proxy = test_different_proxies()
    
    if working_proxy:
        print(f"\n🎯 Proxy funcionou: {working_proxy}")
        print("💡 Use este proxy no script principal")
    else:
        print("\n❌ Nenhuma solução funcionou")
        print("💡 Pode precisar de:")
        print("   - Proxy pago")
        print("   - VPN")
        print("   - Mudar região da AWS")
        print("   - Usar outro provedor de cloud")
