#!/usr/bin/env python3

import sys
import platform
from colorama import init, Fore, Back, Style

init(autoreset=True)

def display_banner():
    banner = f"""
{Fore.RED + Style.BRIGHT}
    ███████╗███╗   ██╗██╗███████╗███████╗███████╗██████╗ 
    ██╔════╝████╗  ██║██║██╔════╝██╔════╝██╔════╝██╔══██╗
    ███████╗██╔██╗ ██║██║█████╗  █████╗  █████╗  ██████╔╝
    ╚════██║██║╚██╗██║██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══██╗
    ███████║██║ ╚████║██║██║      ██╗     ███████╗██║  ██║
    ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝      ╚═╝     ╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}
    {Fore.CYAN + Style.BRIGHT}Website Technology Sniffer v1.0{Style.RESET_ALL}
    {Fore.YELLOW}Discover what powers any website{Style.RESET_ALL}
    {Fore.GREEN}Developed for Security Researchers & Developers{Style.RESET_ALL}
    
    {Fore.MAGENTA} Features:{Style.RESET_ALL}
    {Fore.WHITE}• CMS Detection (WordPress, Drupal, Joomla, etc.)
    • Web Server Identification
    • JavaScript Framework Analysis
    • Analytics & Tracking Detection
    • CDN & Security Header Analysis
    • E-commerce Platform Discovery{Style.RESET_ALL}
    
    {Fore.RED}⚠️  Legal Disclaimer: Use responsibly and only on authorized targets{Style.RESET_ALL}
    """
    
    print(banner)

def print_success(message):
    print(f"{Fore.GREEN}[+] {message}{Style.RESET_ALL}")

def print_error(message):
    print(f"{Fore.RED}[-] {message}{Style.RESET_ALL}")

def print_warning(message):
    print(f"{Fore.YELLOW}[!] {message}{Style.RESET_ALL}")

def print_info(message):
    print(f"{Fore.BLUE}[*] {message}{Style.RESET_ALL}")
