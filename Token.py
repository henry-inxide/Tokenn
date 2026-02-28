#!/usr/bin/env python3
# HENRY PYTHON COMMAND MODE v6.0 | ONE SHOT TOKEN EXTRACTOR
# 🔥 EK BAR RUN - EMAIL/PASS DALO - TOKEN READY 🔥

import requests
import re
import sys
from urllib.parse import quote

print("🔥 HENRY PYTHON TOKEN KILLER v6.0 🔥")
print("=" * 50)

# MOBILE AGENT - FB APP EXACT
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/490.0.0.52.117]',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://m.facebook.com',
    'Referer': 'https://m.facebook.com/'
}

print("📧 Email/Phone dalo:")
email = input("> ").strip()
print("🔑 Password dalo:")
password = input("> ").strip()

print("\n🚀 LOGIN START...")

# STEP 1: MOBILE LOGIN
login_data = {
    'email': email,
    'pass': password,
    'login': 'Log In'
}

session = requests.Session()
login_resp = session.post(
    'https://m.facebook.com/login.php',
    data=login_data,
    headers=headers,
    allow_redirects=True,
    timeout=15
)

print("✅ LOGIN DONE")

# STEP 2: MESSENGER OPEN
print("💬 Messenger scan...")

messenger_resp = session.get(
    'https://www.messenger.com/t/me',
    headers=headers,
    timeout=10
)

graphql_resp = session.get(
    'https://www.facebook.com/api/graphqlquery/MobileMessageThreadWebGraphQL.1576597622539109/',
    headers=headers,
    timeout=10
)

# ALL CONTENT COMBINE
all_content = login_resp.text + messenger_resp.text + str(session.cookies)

# EAAD6V7 EXTRACT
token_pattern = r'EAAD[A-Za-z0-9_-]{247,260}'
tokens = re.findall(token_pattern, all_content)

if tokens:
    best_token = tokens[0]
    print("\n🎉 EAAD6V7 TOKEN PA GAYA! 🎉")
    print("=" * 50)
    print(f"TOKEN: {best_token}")
    print("=" * 50)
    
    # SAVE
    with open('HENRY_EAAD6V7.txt', 'w') as f:
        f.write(best_token)
    print("✅ SAVED: HENRY_EAAD6V7.txt")
    
    # QUICK TEST
    print("🔬 Testing token...")
    test_resp = requests.get(
        f'https://graph.facebook.com/me?access_token={best_token}',
        timeout=10
    )
    if 'id' in test_resp.text:
        print("✅ TOKEN 100% WORKING!")
    else:
        print("⚠️ Token weak hai - blaster me chalega")
        
else:
    print("\n❌ TOKEN NHI MILA")
    print("💡 Messenger me 2 msg bhejo pehle phir try karo")

print("\n🎮 READY FOR BLASTING!")
print("python henry_blaster.py")
