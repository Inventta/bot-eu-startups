#!/usr/bin/env python3
"""
Teste para verificar se VPN resolve o bloqueio
"""

import requests
import subprocess
import time

def check_vpn_status():
    """Verifica se VPN está ativa"""
    try:
        # Verificar IP atual
        response = requests.get('https://ipinfo.io/json', timeout=10)
        ip_info = response.json()
        
        print(f"🌐 IP atual: {ip_info.get('ip', 'N/A')}")
        print(f"🏳️  País: {ip_info.get('country', 'N/A')}")
        print(f"🏢 ISP: {ip_info.get('org', 'N/A')}")
        
        # Se o ISP contém "Amazon" ou "AWS", provavelmente não está usando VPN
        if 'amazon' in ip_info.get('org', '').lower() or 'aws' in ip_info.get('org', '').lower():
            print("⚠️  Parece que ainda está usando IP da AWS")
            return False
        else:
            print("✅ Parece que está usando VPN ou IP diferente da AWS")
            return True
            
    except Exception as e:
        print(f"❌ Erro ao verificar IP: {e}")
        return False

def test_site_access():
    """Testa acesso ao site"""
    url = "https://www.eu-startups.com/directory/conbaseai/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        print(f"\n🔍 Testando acesso ao site...")
        response = requests.get(url, headers=headers, timeout=30)
        
        print(f"✅ Status: {response.status_code}")
        print(f"📏 Tamanho: {len(response.content)} bytes")
        
        if response.status_code == 200:
            print("🎉 SUCESSO! Site acessível!")
            return True
        else:
            print(f"❌ Ainda bloqueado - Status: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def install_vpn_guide():
    """Guia para instalar VPN"""
    print("\n📋 GUIA PARA INSTALAR VPN:")
    print("=" * 50)
    print("1. Instalar OpenVPN:")
    print("   sudo apt-get update")
    print("   sudo apt-get install openvpn")
    print()
    print("2. Opções de VPN gratuita:")
    print("   - ProtonVPN: https://protonvpn.com/")
    print("   - Windscribe: https://windscribe.com/")
    print("   - Hide.me: https://hide.me/")
    print()
    print("3. Opções de VPN paga (mais confiável):")
    print("   - ExpressVPN: https://expressvpn.com/")
    print("   - NordVPN: https://nordvpn.com/")
    print("   - Surfshark: https://surfshark.com/")
    print()
    print("4. Após instalar e conectar VPN:")
    print("   python test_vpn.py")

if __name__ == "__main__":
    print("🚀 Testando VPN...")
    print("=" * 50)
    
    # Verificar status da VPN
    vpn_active = check_vpn_status()
    
    if vpn_active:
        # Testar acesso ao site
        if test_site_access():
            print("\n🎯 VPN funcionou! Pode executar o script principal.")
        else:
            print("\n⚠️  VPN ativa mas site ainda bloqueado.")
            print("💡 Pode precisar de outro servidor VPN ou proxy.")
    else:
        print("\n❌ VPN não detectada ou não ativa.")
        install_vpn_guide()
