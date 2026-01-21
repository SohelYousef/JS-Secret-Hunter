# JS Secret Hunter V2 🕵️‍♂️

**JS Secret Hunter** is an advanced Python tool designed for security researchers to automate the detection of hardcoded secrets in client-side JavaScript.

Unlike simple scanners, **V2** includes a dynamic crawler that parses the HTML of the target website to extract all loaded JavaScript files automatically, ensuring comprehensive coverage.

## Features
- 🕷️ **Dynamic Crawling:** Parses HTML to find all `<script src>` tags automatically.
- 🔍 **Regex-Based Detection:** Identifies Private Keys, API Tokens, AWS Keys, and Database credentials.
- 📂 **Hybrid Scanning:** Combines dynamic crawling with a dictionary of common sensitive filenames (e.g., `config.js`).
- 🛡️ **Safe:** Passive scanning only.

## Installation

```bash
git clone [https://github.com/SohelYousef/JS-Secret-Hunter.git](https://github.com/SohelYousef/JS-Secret-Hunter.git)
cd JS-Secret-Hunter
pip install requests beautifulsoup4

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
