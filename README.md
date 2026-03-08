# Sniffer 

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/expl0itlab/sniffer)](https://github.com/expl0itlab/sniffer/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/expl0itlab/sniffer)](https://github.com/expl0itlab/sniffer/network)
[![Version](https://img.shields.io/badge/version-1.1.0-brightgreen)](https://github.com/expl0itlab/sniffer)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Termux%20%7C%20Windows%20%7C%20macOS-lightgrey)

A powerful website technology detection tool that identifies CMS platforms, frameworks, web servers, analytics tools, databases, and more behind any website.

---

## Features

| Category | Technologies Detected |
|---|---|
| 🛠️ **CMS** | WordPress, Drupal, Joomla, Magento |
| 🌐 **Web Servers** | Apache, Nginx, IIS, LiteSpeed, Caddy, Cloudflare |
| ⚡ **JS Frameworks** | React, Vue.js, Angular, Next.js, Nuxt.js, Svelte, Ember.js, jQuery |
| 💻 **Languages** | PHP, Python, Ruby, Node.js, ASP.NET |
| 📈 **Analytics** | Google Analytics, GTM, Facebook Pixel, Hotjar, Matomo |
| ☁️ **CDN** | Cloudflare, CloudFront, Akamai, Fastly, jsDelivr, Cloudinary |
| 🗄️ **Databases** | MySQL, MongoDB, PostgreSQL, Redis, Elasticsearch |
| 🛒 **E-commerce** | Shopify, WooCommerce, PrestaShop, OpenCart, BigCommerce, Wix |
| 🛡️ **Security Headers** | CSP, HSTS, XSS Protection, COOP, COEP, and more |

**Additional capabilities:**
- 🔁 **Auto HTTP fallback** — retries over HTTP if HTTPS fails
- 🎨 **Colored output** — clean, readable terminal output
- 💾 **JSON export** — save results for further analysis
- 🐛 **Verbose mode** — full debug output including raw headers
- 💻 **Cross-platform** — Linux, Windows, macOS, and Termux (Android)

---

## Quick Start

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Installation

```bash
git clone https://github.com/expl0itlab/sniffer.git
cd sniffer
pip install -r requirements.txt
python sniffer.py
```

---

## Platform Setup

<details>
<summary>🐧 Linux / Ubuntu / Debian</summary>

```bash
sudo apt update && sudo apt install python3 python3-pip git
git clone https://github.com/expl0itlab/sniffer.git
cd sniffer
pip3 install -r requirements.txt
python3 sniffer.py
```
</details>

<details>
<summary>🍎 macOS</summary>

```bash
brew install python git
git clone https://github.com/expl0itlab/sniffer.git
cd sniffer
pip install -r requirements.txt
python sniffer.py
```
</details>

<details>
<summary>🪟 Windows</summary>

```powershell
git clone https://github.com/expl0itlab/sniffer.git
cd sniffer
pip install -r requirements.txt
python sniffer.py
```
</details>

<details>
<summary>📱 Android (Termux)</summary>

```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/expl0itlab/sniffer.git
cd sniffer
pip install -r requirements.txt
python sniffer.py
```
</details>

---

## Usage

```
python sniffer.py [url] [-o OUTPUT] [-v]
```

| Argument | Description |
|---|---|
| `url` | Target website URL (optional — will prompt if omitted) |
| `-o, --output` | Save results to a JSON file |
| `-v, --verbose` | Show raw headers, debug info, and full error traces |

### Examples

```bash
# Basic scan
python sniffer.py example.com

# Scan and save results
python sniffer.py example.com -o results.json

# Verbose output (shows headers, fallback attempts, debug info)
python sniffer.py example.com -v

# Interactive mode
python sniffer.py
```

### Sample Output

```
============================================================
📊  TECHNOLOGY ANALYSIS REPORT
============================================================
🎯  Target    : https://example.com
🔗  Final URL : https://example.com/
📡  Status    : 200
============================================================

🛠️  CMS PLATFORMS:
   ✅  WordPress

🌐  WEB SERVERS:
   ✅  Nginx
   ✅  Cloudflare

⚡  JAVASCRIPT FRAMEWORKS:
   ✅  React
   ✅  jQuery

📈  ANALYTICS TOOLS:
   ✅  Google Analytics
   ✅  Google Tag Manager

🛡️  SECURITY FEATURES:
   ✅  HSTS Enabled: max-age=31536000; includeSubDomains
   ✅  CSP Header: default-src 'self'
   ✅  Clickjacking Protection: SAMEORIGIN

============================================================
Analysis completed successfully!
============================================================
```

---

## Project Structure

```
sniffer/
├── sniffer.py          # Main entry point
├── requirements.txt    # Python dependencies
└── utils/
    ├── __init__.py     # Package metadata & exports
    ├── banner.py       # Colored output helpers
    ├── detector.py     # Technology detection engine
    └── platform_check.py  # Cross-platform requirements check
```

---

## Requirements

```
requests>=2.25.1
colorama>=0.4.4
urllib3>=1.26.0
```

---

## ⚠️ Legal Disclaimer

This tool is intended for **authorized security testing and educational purposes only**.

- Only use Sniffer on websites you own or have explicit written permission to test
- Unauthorized scanning may violate local laws and terms of service
- The authors take no responsibility for misuse of this tool

---

## Join Our Security Community

[![WhatsApp Channel](https://img.shields.io/badge/WhatsApp_Channel-Join_Our_Community-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029VaepfcHBVJkzG6I1y80b)

Stay updated with daily drops on:
- 🛡️ Security tools & techniques
- 🔍 Reconnaissance methods
- 🐍 Python automation scripts
- 📚 Learning resources
- 🚀 Latest project releases

---

## Acknowledgments

- Inspired by tools like [Wappalyzer](https://www.wappalyzer.com/) and [WhatWeb](https://github.com/urbanadventurer/WhatWeb)
- Thanks to the Python open-source community
- **Exploit Lab** — security research and community support
- All contributors and testers who help improve Sniffer

---

<div align="center">

**If you find this tool useful, please give it a ⭐ on GitHub!**

[![GitHub stars](https://img.shields.io/github/stars/expl0itlab/sniffer?style=social)](https://github.com/expl0itlab/sniffer)
[![GitHub forks](https://img.shields.io/github/forks/expl0itlab/sniffer?style=social)](https://github.com/expl0itlab/sniffer)

</div>
