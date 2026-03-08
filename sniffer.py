#!/usr/bin/env python3

import sys
import os
import requests
import argparse
import urllib3
from urllib.parse import urlparse
import json
import time

from utils.banner import display_banner, print_info, print_error, print_success, print_warning
from utils.platform_check import check_platform_requirements
from utils.detector import TechnologyDetector

# Suppress SSL warnings globally when verify=False is used
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Sniffer:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/120.0.0.0 Safari/537.36'
            )
        })
        self.detector = TechnologyDetector()

    def validate_url(self, url):
        """Normalize and validate a URL, defaulting to HTTPS."""
        url = url.strip()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        parsed = urlparse(url)
        if not parsed.netloc:
            raise ValueError(f"Invalid URL provided: '{url}'")

        return url

    def fetch_website_data(self, url):
        """
        Fetch page content, headers and cookies.
        Falls back from HTTPS to HTTP automatically if the HTTPS
        request fails with a connection / SSL error.
        """
        attempts = [url]

        # If the caller supplied HTTPS, also prepare an HTTP fallback
        if url.startswith('https://'):
            attempts.append('http://' + url[len('https://'):])

        last_error = None
        for attempt_url in attempts:
            try:
                if self.verbose:
                    print_info(f"Trying: {attempt_url}")
                else:
                    print_info(f"Fetching data from: {attempt_url}")

                response = self.session.get(
                    attempt_url,
                    timeout=15,
                    verify=False,
                    allow_redirects=True
                )
                response.raise_for_status()

                if self.verbose:
                    print_info(f"Status: {response.status_code}")
                    print_info(f"Content length: {len(response.text)} chars")
                    print_info(f"Response headers: {dict(response.headers)}")

                return {
                    'url': attempt_url,
                    'status_code': response.status_code,
                    'headers': dict(response.headers),
                    'content': response.text,
                    'cookies': dict(response.cookies),
                    'final_url': response.url
                }

            except (requests.exceptions.SSLError,
                    requests.exceptions.ConnectionError) as e:
                last_error = e
                if self.verbose:
                    print_warning(f"Connection failed for {attempt_url}: {e}")
                continue  # try next URL in the list

            except requests.exceptions.Timeout:
                print_error(f"Request timed out for: {attempt_url}")
                return None

            except requests.exceptions.HTTPError as e:
                # Non-2xx response — still worth analysing
                print_warning(f"HTTP error {e.response.status_code} for {attempt_url}")
                return {
                    'url': attempt_url,
                    'status_code': e.response.status_code,
                    'headers': dict(e.response.headers),
                    'content': e.response.text,
                    'cookies': dict(e.response.cookies),
                    'final_url': e.response.url
                }

            except requests.exceptions.RequestException as e:
                print_error(f"Error fetching website: {e}")
                return None

        print_error(f"All connection attempts failed. Last error: {last_error}")
        return None

    def analyze_website(self, url):
        """Fetch a page and run all detectors against it."""
        website_data = self.fetch_website_data(url)
        if not website_data:
            return None

        print_info("Analyzing website technologies...")
        results = self.detector.detect_all(website_data)

        return {
            'target': website_data['url'],
            'final_url': website_data['final_url'],
            'status_code': website_data['status_code'],
            'technologies': results
        }

    def display_results(self, results):
        if not results:
            print_error("No results to display")
            return

        from colorama import Fore, Style

        print("\n" + "=" * 60)
        print(f"{Fore.CYAN + Style.BRIGHT}📊  TECHNOLOGY ANALYSIS REPORT{Style.RESET_ALL}")
        print("=" * 60)
        print(f"🎯  Target    : {results['target']}")
        print(f"🔗  Final URL : {results['final_url']}")
        print(f"📡  Status    : {results['status_code']}")
        print("=" * 60)

        technologies = results['technologies']

        sections = [
            ('cms',                   '🛠️  CMS PLATFORMS'),
            ('web_servers',           '🌐  WEB SERVERS'),
            ('javascript_frameworks', '⚡  JAVASCRIPT FRAMEWORKS'),
            ('programming_languages', '💻  PROGRAMMING LANGUAGES'),
            ('analytics',             '📈  ANALYTICS TOOLS'),
            ('cdn',                   '☁️   CDN PROVIDERS'),
            ('databases',             '🗄️  DATABASES'),          # BUG FIX: was 'db'
            ('ecommerce',             '🛒  E-COMMERCE PLATFORMS'),
            ('security',              '🛡️  SECURITY FEATURES'),
        ]

        found_anything = False
        for key, label in sections:
            items = technologies.get(key, [])
            if items:
                found_anything = True
                print(f"\n{Fore.YELLOW + Style.BRIGHT}{label}:{Style.RESET_ALL}")
                for item in items:
                    print(f"   {Fore.GREEN}✅  {item}{Style.RESET_ALL}")

        if not found_anything:
            print_warning("No technologies detected. The site may use heavy obfuscation.")

        print("\n" + "=" * 60)
        print_success("Analysis completed successfully!")
        print("=" * 60)

    def save_results(self, results, filename=None):
        if not filename:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"sniffer_results_{timestamp}.json"

        try:
            with open(filename, 'w') as f:
                json.dump(results, f, indent=2)
            print_success(f"Results saved to: {filename}")
        except OSError as e:
            print_error(f"Could not save results: {e}")


def main():
    from colorama import init
    init(autoreset=True)  # BUG FIX: initialize colorama for Windows support

    display_banner()
    check_platform_requirements()

    parser = argparse.ArgumentParser(
        description='Sniffer - Website Technology Detection Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python sniffer.py example.com
  python sniffer.py https://example.com -o results.json
  python sniffer.py example.com -v
        """
    )
    parser.add_argument('url', nargs='?', help='Target website URL')
    parser.add_argument('-o', '--output', help='Output file to save results (JSON)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Verbose output (show headers, raw data, debug info)')

    args = parser.parse_args()

    if not args.url:
        args.url = input("\nEnter target URL: ").strip()

    if not args.url:
        print_error("No URL provided. Exiting.")
        sys.exit(1)

    # BUG FIX: pass verbose flag into Sniffer so -v actually does something
    sniffer = Sniffer(verbose=args.verbose)

    try:
        target_url = sniffer.validate_url(args.url)
        print_info(f"Starting analysis for: {target_url}")

        results = sniffer.analyze_website(target_url)

        if results:
            sniffer.display_results(results)

            if args.output:
                sniffer.save_results(results, args.output)
            else:
                save_choice = input("\nSave results to file? (y/n): ").strip().lower()
                if save_choice in ['y', 'yes']:
                    sniffer.save_results(results)
        else:
            print_error("Analysis failed. Please check the URL and try again.")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n")
        print_warning("Operation cancelled by user.")
        sys.exit(0)

    except ValueError as e:
        print_error(str(e))
        sys.exit(1)

    except Exception as e:
        print_error(f"Unexpected error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
