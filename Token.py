#!/usr/bin/env python3
# HENRY MOBILE-ONLY TOKEN EXTRACTOR v8.0
# 🔥 MOBILE ME KOI F12 NAHI - KIWI BROWSER TRICK 🔥

import requests
import re
import webbrowser
import time
import subprocess

print("🔥 HENRY MOBILE v8.0 | NO PC | KIWI BROWSER 🔥")
print("Mobile me F12 nahi? No problem!")

print("""
📱 MOBILE TRICK (30 sec):

1. Play Store → "Kiwi Browser" install karo
2. Kiwi me jao: messenger.com
3. 2 messages bhejo dost ko
4. Menu (3 dots) → More Tools → Developer Tools
5. Console tab → Copy ye command:

document.cookie

6. Yaha paste karo!
""")

cookies = input("\n📋 Kiwi Browser cookies paste karo: ")

if not cookies:
    print("❌ Empty cookies!")
    exit()

print("\n🔍 MOBILE SCAN START...")

# Mobile Kiwi headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 14; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://www.messenger.com',
    'Referer': 'https://www.messenger.com/'
}

session = requests.Session()
session.headers.update(headers)

# Parse mobile cookies
cookie_dict = {}
for cookie in cookies.split(';'):
    if '=' in cookie:
        k, v = cookie.strip().split('=', 1)
        cookie_dict[k] = v
session.cookies.update(cookie_dict)

print("📡 Scanning Messenger endpoints...")

# Mobile safe endpoints
endpoints = [
    'https://www.messenger.com/t/100000000000000',
    'https://www.facebook.com/messages',
    'https://graph.facebook.com/me?fields=id,name'
]

all_data = cookies
for url in endpoints:
    try:
        resp = session.get(url, timeout=7)
        all_data += resp.text
        print("✓", end=' ')
        time.sleep(0.8)
    except:
        pass

# Mobile token patterns
tokens = re.findall(r'EAAD[A-Za-z0-9_-]{247,260}', all_data)

if tokens:
    print("\n\n🎉 MOBILE TOKEN PA GAYA! 🎉")
    token = tokens[0]
    print(f"🔑 {token}")
    
    # Save
    with open('HENRY_MOBILE_TOKEN.txt', 'w') as f:
        f.write(token)
    print("💾 HENRY_MOBILE_TOKEN.txt")
    
    # Test
    test = requests.get(f"https://graph.facebook.com/me?access_token={token}", timeout=5)
    print("✅ WORKING!" if '"id"' in test.text else "⚠️ Blaster try kar")
    
else:
    print("\n❌ No token")
    print("""
🔧 MOBILE FIX:

Kiwi Browser → messenger.com
1. 2 reply bhejo
2. 3 dots → Developer Tools → Console
3. Ye type karo:
   document.cookie
4. Copy full output yaha paste!

Ya fir Termux me ye:
am start -a android.intent.action.VIEW -d "https://www.messenger.com"
""")
