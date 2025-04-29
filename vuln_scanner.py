# vuln_scanner.py
import requests
import re
import settings

headers = {
    "User-Agent": "MASAN-VULNSCAN/1.0 (+https://masan.tools)"
}

cms_patterns = {
    "WordPress": "wp-content|wp-includes|wordpress",
    "Joomla": "content=\"Joomla!",
    "Drupal": "sites/default",
    "Magento": "Mage.Cookies",
}

def detect_cms(html_content):
    for cms, pattern in cms_patterns.items():
        if re.search(pattern, html_content, re.IGNORECASE):
            return cms
    return "Unknown"

def scan_vulns(domain):
    print(f"{settings.COLOR_CYAN}[~] Scanning {domain} for vulnerabilities...{settings.COLOR_END}")

    try:
        r = requests.get(domain, headers=headers, timeout=settings.DEFAULT_TIMEOUT)
        cms = detect_cms(r.text)

        print(f"{settings.COLOR_YELLOW}[i] CMS Detected: {cms}{settings.COLOR_END}")

        if cms == "WordPress":
            wp_scan(domain)
        elif cms == "Joomla":
            joomla_scan(domain)
        elif cms == "Drupal":
            drupal_scan(domain)
        else:
            print(f"{settings.COLOR_RED}[!] No CMS-specific scanning available.{settings.COLOR_END}")
    except Exception as e:
        print(f"{settings.COLOR_RED}[!] Error: {e}{settings.COLOR_END}")

def wp_scan(domain):
    print(f"{settings.COLOR_CYAN}[~] Running WordPress vulnerability checks...{settings.COLOR_END}")
    check_urls = [
        "/readme.html",
        "/wp-admin/install.php",
        "/.git/",
        "/wp-config.php.bak",
    ]
    for path in check_urls:
        try:
            full_url = domain + path
            r = requests.get(full_url, headers=headers, timeout=settings.DEFAULT_TIMEOUT)
            if r.status_code == 200:
                print(f"{settings.COLOR_GREEN}[+] Potential Exposure: {full_url}{settings.COLOR_END}")
        except Exception:
            pass

def joomla_scan(domain):
    print(f"{settings.COLOR_CYAN}[~] Running Joomla vulnerability checks...{settings.COLOR_END}")
    paths = [
        "/administrator/",
        "/configuration.php-dist",
        "/.git/",
    ]
    for path in paths:
        try:
            full_url = domain + path
            r = requests.get(full_url, headers=headers, timeout=settings.DEFAULT_TIMEOUT)
            if r.status_code == 200:
                print(f"{settings.COLOR_GREEN}[+] Potential Exposure: {full_url}{settings.COLOR_END}")
        except Exception:
            pass

def drupal_scan(domain):
    print(f"{settings.COLOR_CYAN}[~] Running Drupal vulnerability checks...{settings.COLOR_END}")
    paths = [
        "/CHANGELOG.txt",
        "/core/INSTALL.txt",
    ]
    for path in paths:
        try:
            full_url = domain + path
            r = requests.get(full_url, headers=headers, timeout=settings.DEFAULT_TIMEOUT)
            if r.status_code == 200:
                print(f"{settings.COLOR_GREEN}[+] Potential Exposure: {full_url}{settings.COLOR_END}")
        except Exception:
            pass

def start_vuln_scan():
    domain = input("Enter full website URL (e.g., https://example.com): ").strip()
    if not domain.startswith("http"):
        domain = "http://" + domain
    scan_vulns(domain)

if __name__ == "__main__":
    start_vuln_scan()
