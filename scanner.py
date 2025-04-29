# scanner.py
import requests
import settings
import os
import time

common_paths = [
    "admin/", "admin.php", "login/", "login.php", "dashboard/",
    ".git/", "config.php", "server-status", "wp-admin/", "robots.txt",
    "sitemap.xml", "phpinfo.php", "backup.zip", "db.sql"
]

headers = {
    "User-Agent": "MASAN-SCANNER/1.0 (+https://masan.tools)"
}

def scan_target(url):
    if not url.startswith("http"):
        url = "http://" + url

    print(f"{settings.COLOR_CYAN}Scanning {url} ...{settings.COLOR_END}\n")
    time.sleep(1)

    found = []

    for path in common_paths:
        full_url = f"{url.rstrip('/')}/{path}"
        try:
            r = requests.get(full_url, headers=headers, timeout=settings.DEFAULT_TIMEOUT)
            if r.status_code == 200:
                print(f"{settings.COLOR_GREEN}[+] Found: {full_url}{settings.COLOR_END}")
                found.append(full_url)
            else:
                print(f"{settings.COLOR_RED}[-] Not Found: {full_url}{settings.COLOR_END}")
        except requests.RequestException:
            print(f"{settings.COLOR_YELLOW}[!] Error accessing {full_url}{settings.COLOR_END}")

    if found:
        save_scan(url, found)
    else:
        print(f"{settings.COLOR_RED}\nNo vulnerable paths found.{settings.COLOR_END}")

def save_scan(url, results):
    folder = "scan_results"
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = os.path.join(folder, url.replace("http://", "").replace("https://", "").replace("/", "_") + ".txt")

    with open(filename, "w") as f:
        for line in results:
            f.write(line + "\n")

    print(f"\n{settings.COLOR_GREEN}Scan saved to {filename}{settings.COLOR_END}")

if __name__ == "__main__":
    target = input("Enter website URL to scan: ")
    scan_target(target)
