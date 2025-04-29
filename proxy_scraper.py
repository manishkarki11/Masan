# proxy_scraper.py
import requests
import threading
import settings

proxies = []
lock = threading.Lock()

proxy_sources = [
    "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
]

def scrape_proxies():
    global proxies
    print(f"{settings.COLOR_CYAN}[~] Scraping proxies...{settings.COLOR_END}")

    for url in proxy_sources:
        try:
            res = requests.get(url, timeout=settings.DEFAULT_TIMEOUT)
            for proxy in res.text.splitlines():
                if proxy.strip():
                    proxies.append(proxy.strip())
        except Exception:
            pass

    print(f"{settings.COLOR_GREEN}[+] Scraped {len(proxies)} proxies.{settings.COLOR_END}")

def check_proxy(proxy):
    try:
        r = requests.get("http://httpbin.org/ip", proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=5)
        if r.status_code == 200:
            with lock:
                with open("valid_proxies.txt", "a") as f:
                    f.write(proxy + "\n")
    except:
        pass

def validate_proxies():
    threads = []
    print(f"{settings.COLOR_CYAN}[~] Checking proxy validity...{settings.COLOR_END}")

    for proxy in proxies:
        t = threading.Thread(target=check_proxy, args=(proxy,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"{settings.COLOR_GREEN}[✓] Valid proxies saved to valid_proxies.txt{settings.COLOR_END}")

def start_scraper():
    scrape_proxies()
    validate_proxies()

if __name__ == "__main__":
    start_scraper()
