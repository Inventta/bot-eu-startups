#!/usr/bin/env python3
"""
Script para testar a conectividade da instância AWS
"""

import requests
import time
from urllib.parse import urlparse

def test_basic_connectivity():
    """Testa conectividade básica com sites conhecidos"""
    print("🌐 Testando conectividade básica...")
    
    test_urls = [
        "https://www.google.com",
        "https://httpbin.org/get",
        "https://www.eu-startups.com",
        "https://www.eu-startups.com/directory/"
    ]
    
    for url in test_urls:
        try:
            print(f"\n🔍 Testando: {url}")
            start_time = time.time()
            
            response = requests.get(url, timeout=10)
            end_time = time.time()
            
            print(f"✅ Status: {response.status_code}")
            print(f"⏱️  Tempo: {end_time - start_time:.2f}s")
            print(f"📏 Tamanho: {len(response.content)} bytes")
            
            if response.status_code == 200:
                print("✅ Conectividade OK!")
            else:
                print(f"⚠️  Status não esperado: {response.status_code}")
                
        except requests.exceptions.Timeout:
            print("❌ Timeout - Site não respondeu em 10 segundos")
        except requests.exceptions.ConnectionError as e:
            print(f"❌ Erro de conexão: {e}")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

def test_specific_site():
    """Testa o site específico que está falhando"""
    print("\n🎯 Testando site específico que está falhando...")
    
    test_url = "https://www.eu-startups.com/directory/portf0lio/"
    
    try:
        print(f"🔍 Testando: {test_url}")
        
        # Teste com headers para simular um navegador
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(test_url, headers=headers, timeout=10)
        
        print(f"✅ Status: {response.status_code}")
        print(f"📏 Tamanho: {len(response.content)} bytes")
        
        if response.status_code == 200:
            print("✅ Site acessível!")
            print("🔍 Verificando se o conteúdo contém os elementos esperados...")
            
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Verificar se existem os elementos que o script procura
            field_labels = soup.find_all('span', class_='field-label')
            print(f"📋 Encontrados {len(field_labels)} field-labels")
            
            if field_labels:
                print("✅ Estrutura HTML esperada encontrada!")
                for label in field_labels[:3]:  # Mostrar os primeiros 3
                    print(f"   - {label.text.strip()}")
            else:
                print("⚠️  Estrutura HTML não encontrada - site pode ter mudado")
                
        else:
            print(f"❌ Status não esperado: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Erro: {e}")

def test_network_config():
    """Testa configurações de rede"""
    print("\n🔧 Testando configurações de rede...")
    
    try:
        import socket
        
        # Teste DNS
        print("🔍 Testando resolução DNS...")
        ip = socket.gethostbyname("www.eu-startups.com")
        print(f"✅ DNS OK - IP: {ip}")
        
        # Teste porta 80/443
        print("🔍 Testando portas...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        
        result = sock.connect_ex(('www.eu-startups.com', 443))
        if result == 0:
            print("✅ Porta 443 (HTTPS) acessível")
        else:
            print("❌ Porta 443 (HTTPS) não acessível")
            
        sock.close()
        
    except Exception as e:
        print(f"❌ Erro no teste de rede: {e}")

if __name__ == "__main__":
    print("🚀 Iniciando testes de conectividade...")
    print("=" * 50)
    
    test_basic_connectivity()
    test_specific_site()
    test_network_config()
    
    print("\n" + "=" * 50)
    print("🎯 Testes concluídos!")
