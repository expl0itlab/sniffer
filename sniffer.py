#!/usr/bin/env python3

import sys
import os
import requests
import argparse
from urllib.parse import urlparse
import json
import time
from utils.banner import display_banner
from utils.platform_check import check_platform_requirements
from utils.detector import TechnologyDetector

class Sniffer:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.detector = TechnologyDetector()
    
    def validate_url(self, url):
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        parsed = urlparse(url)
        if not parsed.netloc:
            raise ValueError("Invalid URL provided")
        
        return url
    
    def fetch_website_data(self, url):
        try:
            print(f"[*] Fetching data from: {url}")
            response = self.session.get(url, timeout=10, verify=False)
            response.raise_for_status()
            
            return {
                'url': url,
                'status_code': response.status_code,
                'headers': dict(response.headers),
                'content': response.text,
                'cookies': dict(response.cookies),
                'final_url': response.url
            }
        except requests.exceptions.RequestException as e:
            print(f"[-] Error fetching website: {e}")
            return None
    
    def analyze_website(self, url):
        website_data = self.fetch_website_data(url)
        if not website_data:
            return None
        
        print("[*] Analyzing website technologies...")
        
        results = self.detector.detect_all(website_data)
        
        return {
            'target': website_data['url'],
            'final_url': website_data['final_url'],
            'status_code': website_data['status_code'],
            'technologies': results
        }
    
    def display_results(self, results):
        if not results:
            print("[-] No results to display")
            return
        
        print("\n" + "="*60)
        print(f"📊 TECHNOLOGY ANALYSIS REPORT")
        print("="*60)
        print(f"🎯 Target: {results['target']}")
        print(f"🔗 Final URL: {results['final_url']}")
        print(f"📡 Status Code: {results['status_code']}")
        print("="*60)
        
        technologies = results['technologies']
        
        if technologies['cms']:
            print("\n🛠️  CMS PLATFORMS:")
            for cms in technologies['cms']:
                print(f"   ✅ {cms}")
        
        if technologies['web_servers']:
            print("\n🌐 WEB SERVERS:")
            for server in technologies['web_servers']:
                print(f"   ✅ {server}")
        
        if technologies['javascript_frameworks']:
            print("\n⚡ JAVASCRIPT FRAMEWORKS:")
            for framework in technologies['javascript_frameworks']:
                print(f"   ✅ {framework}")
        
        if technologies['programming_languages']:
            print("\n💻 PROGRAMMING LANGUAGES:")
            for lang in technologies['programming_languages']:
                print(f"   ✅ {lang}")
        
        if technologies['analytics']:
            print("\n📈 ANALYTICS TOOLS:")
            for analytic in technologies['analytics']:
                print(f"   ✅ {analytic}")
        
        if technologies['cdn']:
            print("\n☁️  CDN PROVIDERS:")
            for cdn in technologies['cdn']:
                print(f"   ✅ {cdn}")
        
        if technologies['databases']:
            print("\n🗄️  DATABASES:")
            for db in technologies['db']:
                print(f"   ✅ {db}")
        
        if technologies['ecommerce']:
            print("\n🛒 E-COMMERCE PLATFORMS:")
            for ecom in technologies['ecommerce']:
                print(f"   ✅ {ecom}")
        
        if technologies['security']:
            print("\n🛡️  SECURITY FEATURES:")
            for security in technologies['security']:
                print(f"   ✅ {security}")
        
        print("\n" + "="*60)
        print("Analysis completed successfully!")
        print("="*60)
    
    def save_results(self, results, filename=None):
        if not filename:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"sniffer_results_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"[+] Results saved to: {filename}")

def main():
    display_banner()
    
    check_platform_requirements()
    
    parser = argparse.ArgumentParser(description='Sniffer - Website Technology Detection Tool')
    parser.add_argument('url', nargs='?', help='Target website URL')
    parser.add_argument('-o', '--output', help='Output file to save results (JSON)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    if not args.url:
        args.url = input("\nEnter target URL: ").strip()
    
    if not args.url:
        print("[-] No URL provided. Exiting.")
        sys.exit(1)
    
    sniffer = Sniffer()
    
    try:
        target_url = sniffer.validate_url(args.url)
        
        print(f"[*] Starting analysis for: {target_url}")
        
        results = sniffer.analyze_website(target_url)
        
        if results:
            sniffer.display_results(results)
            
            if args.output:
                sniffer.save_results(results, args.output)
            else:
                save_choice = input("\nSave results to file? (y/n): ").lower()
                if save_choice in ['y', 'yes']:
                    sniffer.save_results(results)
        
        else:
            print("[-] Analysis failed. Please check the URL and try again.")
    
    except KeyboardInterrupt:
        print("\n[-] Operation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"[-] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()