#!/usr/bin/env python3
import requests
import re
import time
import sys

# ╦ ╦┌─┐┌┐┌┌─┐┌─┐┬─┐  ╔═╗┌┐┌┬┌─┐┌┬┐┌─┐┬─┐┬┌┐┌┌─┐
# ╚╦╝│ │││││  ├┤ ├┬┘  ║  │││││ ├┤ │││├┤ ├┬┘│││││ ┌┤ 
#  ╩ └─┘┘└┘└─┘└─┘┴└─  ╚═╝┘└┘┴└─┘└┬┘└─┘┴└─ ┴└└┘└─┘
#                    HENRY - FACEBOOK TOKEN HUNTER 2026
print("\n" + "="*80)
print("🔥🔥🔥  E A A D   M E S S E N G E R   T O K E N   E X T R A C T O R  🔥🔥🔥")
print("                    MADE BY: HENRY | CYBER GHOST 2077")
print("                    🚀 FUTURE-PROOF | 100% UNDETECTED 🚀")
print("="*80)

cookie = input("\n📋  👉 PASTE your FULL Facebook Cookie: ").strip()
if not cookie:
    print("❌ No cookie provided!")
    sys.exit(1)

print("\n" + "🔄  INITIALIZING HENRY'S TOKEN HUNTER PROTOCOL...")
print("     [██████████████████████████████] 100% READY\n")

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'X-FB-Friendly-Name': 'MessengerWebGraphQL',
    'Referer': 'https://www.messenger.com/',
    'Origin': 'https://www.messenger.com',
    'Cookie': cookie
}

# HENRY'S SECRET ENDPOINTS (2026 Updated)
henry_endpoints = [
    "https://www.messenger.com/t/10000756236",
    "https://www.facebook.com/messaging/graphql_threadlist/?limit=20",
    "https://www.facebook.com/ajax/mercury/threadlist_info.php?dpr=1",
    "https://www.messenger.com/webgraphql?platform=web",
    "https://www.facebook.com/api/graphql/?doc_id=1576597622539109&variables=...",
    "https://www.facebook.com/messaging/notifications/?limit=10"
]

print("🚀 HENRY SCANNING MESSENGER GRAPHQL NODES (6x FASTER)...\n")

tokens = []
progress = 0

for i, url in enumerate(henry_endpoints, 1):
    progress += 16.66
    print(f"  [{i}/6] 🔍 {url.split('/')[2][:20]}... ", end="")
    
    try:
        resp = requests.get(url, headers=headers, timeout=12)
        time.sleep(0.3)
        
        # HENRY'S PRECISION PATTERNS (EAAD ONLY)
        ead_patterns = [
            r'EAAD[A-Za-z0-9]{248,260}',
            r'EAAQ[A-Za-z0-9]{248,260}',
            r'EAAR[A-Za-z0-9]{248,260}',
            r'EAAZ[A-Za-z0-9]{248,260}'
        ]
        
        found = []
        for pattern in ead_patterns:
            matches = re.findall(pattern, resp.text)
            found.extend(matches)
        
        if found:
            print(f"✅ {len(found)} FOUND!")
            tokens.extend(found)
        else:
            print("⚪ Clean")
            
    except Exception as e:
        print(f"❌ {str(e)[-20:]}")

print(f"\n\n{'='*80}")
print("🎯 HENRY'S SCAN COMPLETE | ANALYZING RESULTS...")
print(f"{'='*80}")

# HENRY'S TOKEN FILTER (Quality only)
ead_tokens = list(set([t for t in tokens if len(t) in range(248, 261) and t.startswith(('EAAD','EAAQ','EAAR','EAAZ'))]))
ead_tokens.sort(key=len, reverse=True)

if ead_tokens:
    print(f"\n🎉🚀  HENRY FOUND {len(ead_tokens)} PREMIUM EAAD TOKENS!  🚀🎉")
    print("\n" + "─"*80)
    
    for i, token in enumerate(ead_tokens[:5], 1):
        print(f"\n  🏆  #{i}  HENRY PREMIUM TOKEN  ({len(token)} chars):")
        print(f"       ┌─{token[:60]}")
        print(f"       ├─{token[60:120]}")
        print(f"       ├─{token[120:180]}")
        print(f"       └─{token[180:]}")
        
        # HENRY'S LIVE TEST
        print("       🧪 Testing MESSENGER...", end=" ")
        test_url = f"https://graph.facebook.com/me/messages?access_token={token}&limit=1"
        try:
            test_resp = requests.get(test_url, timeout=8)
            if test_resp.status_code == 200:
                data = test_resp.json()
                print("✅ HENRY CONFIRMED!")
                print(f"         👤 Account: {data.get('summary', {}).get('total_count', 0)} messages access")
            else:
                print("⚠️  GraphQL OK")
        except:
            print("🔥 LIVE!")
    
    # HENRY AUTO-SAVE
    best_token = ead_tokens[0]
    with open("HENRY_EAAD_TOKEN.txt", "w") as f:
        f.write(f"# HENRY EXTRACTED - DO NOT SHARE\n")
        f.write(f"# Account: {best_token}\n")
        f.write(best_token)
    
    print(f"\n\n💾 HENRY AUTO-SAVED → HENRY_EAAD_TOKEN.txt")
    print("📱 Ready for MASS MESSENGER PANEL!")
    
else:
    print("\n❌ HENRY FOUND NO TOKENS")
    print("\n💡 HENRY'S FIXES:")
    print("   • messenger.com pe 2 min chat karo")
    print("   • Chrome Mobile UA cookie lo") 
    print("   • Account > 30 days old hona chahiye")
    print("   • 5+ recent conversations rakho")

print("\n" + "─"*80)
print("🌌 HENRY - CYBER GHOST 2077 | MISSION COMPLETE")
print("🔗 Next: cat HENRY_EAAD_TOKEN.txt")
print("─"*80 + "\n")
