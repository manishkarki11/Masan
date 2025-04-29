# cf_bypass.py
import requests
import socket
import settings
import time
import re

headers = {
    "User-Agent": "MASAN-CFBYPASS/1.0 (+https://masan.tools)"
}

def find_origin_ip(domain):
    print(f"{settings.COLOR_CYAN}[~] Attempting to find real IP for {domain}{settings.COLOR_END}")

    try:
        ip = socket.gethostbyname(domain)
        print(f"{settings.COLOR_GREEN}[+] Resolved IP: {ip}{settings.COLOR_END}")
        return ip
    except socket.error:
        print(f"{settings.COLOR_RED}[!] Could not resolve domain.{settings.COLOR_END}")
        return None

def leak_methods(domain):
    leaked = []

    try:
        # Common Subdomains
        subdomains = ["direct", "origin", "dev", "test", "staging", "server", "cpanel"]
        for sub in subdomains:
            subdomain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(subdomain)
                print(f"{settings.COLOR_GREEN}[+] Leaked Subdomain IP: {subdomain} => {ip}{settings.COLOR_END}")
                leaked.append((subdomain, ip))
            except socket.error:
                pass
    except Exception as e:
        print(f"{settings.COLOR_RED}Error scanning subdomains: {e}{settings.COLOR_END}")

    return leaked

def basic_cf_bypass(domain):
    print(f"{settings.COLOR_CYAN}[~] Trying HTTP Bypass...{settings.COLOR_END}")
    url = "http://" + domain

    try:
        r = requests.get(url, headers=headers, timeout=settings.DEFAULT_TIMEOUT)
        if "Checking your browser before accessing" in r.text:
            print(f"{settings.COLOR_RED}[!] Cloudflare JS Challenge detected!{settings.COLOR_END}")
        else:
            print(f"{settings.COLOR_GREEN}[+] Page loaded, bypass may have succeeded!{settings.COLOR_END}")
    except requests.RequestException:
        print(f"{settings.COLOR_RED}[!] Could not access {url}{settings.COLOR_END}")

def start_cf_bypass(target):
    domain = target.replace("http://", "").replace("https://", "").split('/')[0]
    find_origin_ip(domain)
    leak_methods(domain)
    basic_cf_bypass(domain)

if __name__ == "__main__":
    target = input("Enter website to bypass Cloudflare: ")
    start_cf_bypass(target)
