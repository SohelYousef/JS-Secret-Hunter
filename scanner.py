import requests
import re
import argparse
import sys
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

# JS Secret Hunter V2
# Author: Sohel Yousef
# Advanced Features: HTML Parsing & Dynamic JS Extraction

BANNER = """
    #######################################################
    #        JS SECRET HUNTER V2 - Sohel Yousef           #
    #   Automated Crawler & Sensitive Data Scanner        #
    #######################################################
"""

# Common sensitive files (Backup list if crawling misses them)
COMMON_FILES = [
    "config.js", "env.js", "secrets.js", "wallet.js", 
    "constants.js", "app-config.js", "api.js"
]

# Regex Patterns for Secrets
PATTERNS = {
    "ETH_PRIVATE_KEY": r"0x[a-fA-F0-9]{64}",
    "GENERIC_API_KEY": r"(?i)(api_key|apikey|secret|token)\s*[:=]\s*['\"]([a-zA-Z0-9_\-]{10,})['\"]",
    "AWS_ACCESS_KEY": r"AKIA[0-9A-Z]{16}",
    "GOOGLE_API_KEY": r"AIza[0-9A-Za-z\\-_]{35}",
    "FIREBASE_CONFIG": r"firebaseConfig",
    "DB_PASSWORD": r"(?i)(password|passwd|pwd)\s*[:=]\s*['\"]([^'\"]+)['\"]"
}

def get_js_links(base_url):
    """Crawl the homepage to extract all <script src> links"""
    print(f"[*] Crawling {base_url} for JavaScript files...")
    js_links = set()
    
    try:
        response = requests.get(base_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            scripts = soup.find_all('script')
            
            for script in scripts:
                if script.get('src'):
                    full_url = urljoin(base_url, script.get('src'))
                    # Ensure we scan valid JS files belonging to the domain (optional filter)
                    js_links.add(full_url)
            
            print(f"[+] Found {len(js_links)} unique JS files via crawling.")
        else:
            print(f"[!] Failed to crawl page. Status: {response.status_code}")
            
    except Exception as e:
        print(f"[!] Crawling Error: {e}")
        
    return js_links

def scan_file(url):
    """Scan a single URL for secrets"""
    print(f"[*] Scanning: {url}")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            content = response.text
            found_anything = False
            
            for name, pattern in PATTERNS.items():
                matches = re.findall(pattern, content)
                for match in matches:
                    print(f"    [!] CRITICAL: Found {name}")
                    # Handle tuple matches from regex groups
                    val = match[0] if isinstance(match, tuple) else match
                    # Masking output
                    masked = str(val)[:5] + "..." + str(val)[-5:] if len(str(val)) > 10 else "***"
                    print(f"    [>] Value: {masked}")
                    found_anything = True
            
            if not found_anything:
                pass # Silent on clean files to reduce noise
        else:
            print(f"    [x] Skipped (Status: {response.status_code})")
            
    except Exception as e:
        print(f"    [!] Connection Error: {e}")

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="Scan JS files for secrets")
    parser.add_argument("--url", required=True, help="Base URL of the target website")
    args = parser.parse_args()

    target_url = args.url.rstrip("/")
    
    # Phase 1: Dynamic Crawling
    extracted_links = get_js_links(target_url)
    
    # Phase 2: Add Common Files (Dictionary Attack)
    for filename in COMMON_FILES:
        full_url = urljoin(target_url + "/", filename)
        extracted_links.add(full_url)

    print(f"\n[*] Total files to scan: {len(extracted_links)}")
    print("[*] Starting Heuristic Scan...\n")

    for link in extracted_links:
        scan_file(link)
    
    print("\n[*] Scan Completed.")

if __name__ == "__main__":
    main()
