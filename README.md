# JS-Secret-Hunter
Automated Python scanner to detect hardcoded secrets (Private Keys, API Tokens) in client-side JavaScript files.
# JS Secret Hunter 🕵️‍♂️

**JS Secret Hunter** is a lightweight Python tool designed for security researchers and Bug Bounty hunters. It automates the process of scanning client-side JavaScript files for hardcoded sensitive information.

Many developers accidentally leave critical data (like Private Keys, API tokens, or AWS credentials) in public `.js` files (e.g., `wallet.js`, `config.js`). This tool hunts them down.

## Features
- 🔍 **Regex-Based Detection:** Scans for Ethereum Private Keys, AWS Keys, Google API Keys, and generic tokens.
- ⚡ **Fast Scanning:** Checks common file paths automatically.
- 🛡️ **Safe:** Identifies secrets without exploiting them.

## Installation

```bash
git clone [https://github.com/SohelYousef/JS-Secret-Hunter.git](https://github.com/SohelYousef/JS-Secret-Hunter.git)
cd JS-Secret-Hunter
pip install requests

python3 scanner.py --url [https://target-website.com](https://target-website.com)


Disclaimer
This tool is for educational purposes and authorized security assessments only. The author is not responsible for any misuse.
