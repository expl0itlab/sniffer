#!/usr/bin/env python3
import platform
from colorama import init, Fore, Style
init(autoreset=True)
def display_banner():
    banner = f"""
{Fore.RED + Style.BRIGHT}
    ███████╗███╗   ██╗██╗███████╗███████╗███████╗██████╗ 
    ██╔════╝████╗  ██║██║██╔════╝██╔════╝██╔════╝██╔══██╗
    ███████╗██╔██╗ ██║██║█████╗  █████╗  █████╗  ██████╔╝
    ╚════██║██║╚██╗██║██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══██╗
    ███████║██║ ╚████║██║██║     ██╗     ███████╗██║  ██║
    ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}
    {Fore.CYAN + Style.BRIGHT}Website Technology Sniffer v1.1{Style.RESET_ALL}
    {Fore.YELLOW}Discover what powers any website{Style.RESET_ALL}
    {Fore.GREEN}Developed for Security Researchers & Developers{Style.RESET_ALL}
   {Style.RESET_ALL}
    """
    print(banner)
def print_success(message):
    print(f"{Fore.GREEN}[+] {message}{Style.RESET_ALL}")
def print_error(message):
    print(f"{Fore.RED}[-] {message}{Style.RESET_ALL}")
def print_warning(message):
    print(f"{Fore.YELLOW}[!] {message}{Style.RESET_ALL}")
def print_info(message):
    print(f"{Fore.CYAN}[*] {message}{Style.RESET_ALL}")
