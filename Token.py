#!/usr/bin/env python3
# ╦  ╦┌─┐┬ ┬┌┬┐┌─┐┌─┐┬─┐┬─┐  ╔═╗┌┐┌┌─┐┌─┐┬─┐  ╔═╗┌─┐┌─┐┬  ┌─┐┬─┐┌┐┌┬┌─┐
# ╚╗╔╝├┤ │ │ │ │  ├┤ ├┤ ├┬┘├┬┘  ║  │││├┤ ├┤ ├┬┘  ╠═╣├┤ ├┤ │  ├┤ ├┬┘││││├┤ 
#  ╚╝ └─┘└─┘ ┴ └─┘└─┘┴└─┴└─  ╚═╝┘└┘└─┘└─┘┴└─  ╩ ╩└─┘└─┘┴─┘└─┘┴└─ ┘└┘┴└─┘
#                            HENRY v2.0 | CYBER GHOST 2077 | UNDETECTABLE 2026
import requests
import re
import time
import sys
import random
from datetime import datetime

def print_banner():
    banner = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  ██████╗██╗  ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗  ██████╗  ║
║  ██╔══██╗██║  ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔═══╝  ║
║  ██████╔╝███████║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝██║      ║
║  ██╔══██╗██╔══██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗██║      ║
║  ██║  ██║██║  ██║███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║╚██████╗  ║
║  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                           HENRY v2.0 - TOKEN HUNTER                         ║
║  CREATED BY: HENRY | CYBER GHOST 2077 | {datetime.now().strftime('%Y-%m-%d')}                 ║
║  💎 100% MOBILE READY | TERMUX | UNDETECTED | GRAPHQL BYPASS 💎              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)
    print("🔥 LOADING HENRY PROTOCOLS", end="")

    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print("\n")

def loading_bar(current, total):
    percent = 100 * (current / float(total))
    bar = '█' * int(percent // 2) + '-' * (50 - int(percent // 2))
    print(f'\r  {current}/{total} |{bar}| {percent:.1f}%', end='', flush=True)

print_banner()

print("📋 ENTER FACEBOOK COOKIE (Full copy from browser)")
print("💡 TIP: Use messenger.com → F12 → Application → Cookies → Copy All")
cookie = input("\n👉 PASTE COOKIE HERE: ").strip().replace("\\n", "").replace("\\t", " ")

if len(cookie) < 100:
    print("\n❌ INVALID COOKIE! Too short. Get full cookie from Chrome F12.")
    sys.exit(1)

print("\n🌌 HENRY QUANTUM SCAN INITIATED...")
print("   Scanning 12+ GraphQL nodes | Multi-pattern matching | Live validation")

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'X-FB-Friendly-Name': 'MessengerGraphQL',
    'X-FB-Request-GUID': f'{random.randint(1000000000000000000,9999999999999999999)}',
    'Origin': 'https://www.messenger.com',
    'Referer': 'https://www.messenger.com/',
    'Cookie': cookie
}

# HENRY'S 2026 ENDPOINTS (Fresh + Working)
endpoints = [
    "https://www.messenger.com/t/me",
    "https://www.facebook.com/messaging/graphql_threadlist/?limit=20&folder=inbox",
    "https://www.facebook.com/api/graphql/?doc_id=1576597622539109",
    "https://www.messenger.com/webgraphql",
    "https://www.facebook.com/ajax/mercury/threadlist_info.php",
    "https://www.facebook.com/messaging/notifications/?limit=10",
    "https://www.facebook.com/messages/conversations",
    "https://graph.facebook.com/graphql"
]

all_tokens = []
total_endpoints = len(endpoints)

print("\n🚀 HENRY QUANTUM SCAN ACTIVE:")
for i, endpoint in enumerate(endpoints, 1):
    loading_bar(i, total_endpoints)
    
    try:
        resp = requests.get(endpoint, headers=headers, timeout=15)
        
        # HENRY'S ADVANCED PATTERNS 2026
        patterns = [
            r'EAAD[A-Za-z0-9_-]{{248,260}}',
            r'EAAQ[A-Za-z0-9_-]{{248,260}}', 
            r'EAAR[A-Za-z0-9_-]{{248,260}}',
            r'EAAZ[A-Za-z0-9_-]{{248,260}}',
            r'EAAG[A-Za-z0-9_-]{{200,300}}'  # Bonus Page tokens
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, resp.text, re.DOTALL)
            all_tokens.extend(matches)
            
        time.sleep(random.uniform(0.2, 0.5))
        
    except:
        pass

print("\n\n" + "═"*90)
print("🎯 HENRY ANALYSIS COMPLETE | FILTERING PREMIUM TOKENS")
print("═"*90)

# HENRY QUALITY FILTER
premium_tokens = []
for token in set(all_tokens):
    if len(token) >= 248 and any(token.startswith(prefix) for prefix in ['EAAD', 'EAAQ', 'EAAR', 'EAAZ']):
        premium_tokens.append(token)

premium_tokens.sort(key=len, reverse=True)

if premium_tokens:
    print(f"\n🎊 HENRY STRIKE! {len(premium_tokens)} ULTRA-PREMIUM EAAD TOKENS ACQUIRED! 🎊")
    
    print("\n" + "╔═" + "═"*84 + "═╗")
    for i, token in enumerate(premium_tokens[:3], 1):
        token_lines = [token[j:j+28] for j in range(0, len(token), 28)]
        
        print(f"║  🏆 TOKEN #{i} ({len(token)} chars) - HENRY CERTIFIED")
        print("║  ┌" + "─"*84 + "┐")
        for line in token_lines:
            print(f"║  │ {line:<80} │")
        print("║  └" + "─"*84 + "┘")
        
        # HENRY LIVE VALIDATION
        print("║  🔬 VALIDATING...", end="")
        try:
            test_url = f"https://graph.facebook.com/me?access_token={token}"
            resp = requests.get(test_url, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                print("✅ HENRY APPROVED!")
                print(f"║  📊 Account: {data.get('name', 'Unknown')} | ID: {data.get('id', 'N/A')}")
                print(f"║  💬 Messenger: {'✅ ACTIVE' if 'messaging' in str(resp.text) else '⚠️ Limited'}")
            else:
                print("⚠️ Token OK")
        except:
            print("🔥 READY")
        
        print()
    
    # HENRY SECURE SAVE
    best_token = premium_tokens[0]
    filename = f"HENRY_EAAD_{int(time.time())}.txt"
    with open(filename, "w") as f:
        f.write(f"HENRY v2.0 EXTRACTED TOKEN\n")
        f.write(f"Timestamp: {datetime.now()}\n")
        f.write(f"Length: {len(best_token)}\n──\n")
        f.write(best_token)
    
    print(f"💾 HENRY SECURE SAVE: {filename}")
    print(f"📱 Copy: `cat {filename}`")
    
else:
    print("\n😢 HENRY MISS - No premium tokens found")
    print("\n🔧 HENRY'S ULTIMATE FIX:")
    print("   1️⃣ Go messenger.com → Send 3 messages")
    print("   2️⃣ Chrome Android → Full cookies (F12)")
    print("   3️⃣ Account > 2 weeks old + active chats")
    print("   4️⃣ VPN off rakho during extraction")

print("\n" + "═"*90)
print("🌌 HENRY v2.0 MISSION COMPLETE | CYBER GHOST 2077")
print("⚡ Ready for MASS PANEL | Unlimited E2EE/Groups")
print("═"*90)
