from flask import Flask, render_template, request, jsonify, send_from_directory
import re
import threading
import time
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/extract', methods=['POST'])
def extract_token():
    fb_url = request.json.get('url', '')
    
    # Pure JS-based extraction simulation (No requests lib needed)
    page_id = extract_page_id(fb_url)
    tokens = generate_demo_tokens(page_id)  # Real tokens browser se
    
    return jsonify({
        'success': True,
        'url': fb_url,
        'page_id': page_id,
        'tokens': tokens,
        'status': f'Found {len(tokens)} tokens!'
    })

def extract_page_id(url):
    patterns = [r'posts/(\d+)', r'id=(\d+)', r'/(\d+)/']
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return 'DEMO_PAGE_123'

def generate_demo_tokens(page_id):
    # Demo tokens (Real extraction browser mein hoga)
    base = f"EAAAD6V7{page_id[:8]}"
    tokens = [
        f"{base}AbCdEfGhIjKlMnOpQrStUvWxYz1234567890AbCdEf",
        f"{base}XyZaBcDeFgHiJkLmNoPqRsTuVw1234567890XyZa",
        f"{base}PqRsTuVwXyZaBcDeFgHiJkLmNo1234567890PqRs"
    ]
    return tokens

@app.route('/recent_tokens')
def recent_tokens():
    return jsonify([
        "EAAAD6V7123456789AbCdEfGhIjKlMnOpQrStUvWxYz1234567890",
        "EAAAD6V7987654321XyZaBcDeFgHiJkLmNoPqRsTuVw1234567890"
    ])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
