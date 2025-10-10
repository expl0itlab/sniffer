# Sniffer 

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/exploitarium/sniffer)](https://github.com/exploitarium/sniffer/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/exploitarium/sniffer)](https://github.com/exploitarium/sniffer/network)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Termux%20%7C%20Windows%20%7C%20macOS-lightgrey)

A powerful website technology detection tool that identifies CMS platforms, frameworks, web servers, analytics tools, and more behind any website.


## Features

🛠️ **CMS Detection** (WordPress, Drupal, Joomla, Magento, Shopify)

🌐 **Web Server Identification** (Apache, Nginx, IIS, Cloudflare)

⚡ **JavaScript Framework Analysis** (React, Vue.js, Angular, jQuery)

📈 **Analytics & Tracking Detection** (Google Analytics, Facebook Pixel, GTM)

☁️ **CDN & Infrastructure Analysis** (Cloudflare, CloudFront, Akamai)

🛒 **E-commerce Platform Discovery** (WooCommerce, Shopify, PrestaShop)

🛡️ **Security Header Analysis** (CSP, HSTS, XSS Protection)

💻 **Cross-Platform** - Works on Linux, Windows, macOS, and Termux (Android)

🎨 **Colored Output** - Beautiful, readable console output

💾 **JSON Export** - Save results for further analysis

## Quick Start

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/exploitarium/sniffer.git
cd sniffer

# Install dependencies
pip install -r requirements.txt

# Run the tool
python sniffer.py
```
### Linux/Ubuntu/Debian 

```bash
sudo apt update
sudo apt install python3 python3-pip git
git clone https://github.com/exploitarium/sniffer.git
cd sniffer
pip3 install -r requirements.txt
python3 sniffer.py
```
### macOS 

```bash
# Install Python and Git
brew install python git
git clone https://github.com/exploitarium/sniffer.git
cd sniffer
pip install -r requirements.txt
python sniffer.py
```
### Windows 

```bash
# Using PowerShell
git clone https://github.com/exploitarium/sniffer.git
cd sniffer
pip install -r requirements.txt
python sniffer.py
```
### Android(Termux) 

```bash
pkg update && pkg upgrade
pkg install python git
pip install requests colorama
git clone https://github.com/exploitarium/sniffer.git
cd sniffer
python sniffer.py
```
### Advanced Options 

```bash
# Save results to JSON file
python sniffer.py example.com -o results.json

# Verbose output
python sniffer.py example.com -v

# Interactive mode (no arguments)
python sniffer.py
```
# ⚠️ Legal Disclaimer

This tool is for authorized testing only. Use responsibly.

---

## Join Our Security Community

Stay updated with the latest security tools, tutorials, and resources:

<div align="left">

### **Exploit Lab WhatsApp Channel**

[![WhatsApp Channel](https://img.shields.io/badge/WhatsApp_Channel-Join_Our_Community-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029VaepfcHBVJkzG6I1y80b)

**Get daily updates on:**

 🛡️  Security Tools & Techniques

 🔍  Reconnaissance Methods  

 🐍  Python Automation Scripts

 📚  Learning Resources

 🚀  Latest Project Releases


</div>



## Acknowledgments

- Inspired by various open-source reconnaissance tools
- Thanks to the Python community for excellent libraries
- **Exploit Lab (Exploitarium)** - For security research and community support
- Contributors and testers who help improve Sniffer


<div align="center">

**If you find this tool useful, please give it a star on GitHub!**

[![GitHub stars](https://img.shields.io/github/stars/exploitarium/sniffer?style=social)](https://github.com/exploitarium/sniffer)
[![GitHub forks](https://img.shields.io/github/forks/exploitarium/sniffer?style=social)](https://github.com/exploitarium/sniffer)

</div>
