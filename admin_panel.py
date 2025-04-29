# admin_panel.py
import getpass
import settings
import os
import sys
import time

def login():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{settings.COLOR_CYAN}Welcome to Admin Panel - MASAN{settings.COLOR_END}")
    username = input("Enter Admin Username: ")
    password = getpass.getpass("Enter Admin Password: ")

    if username == settings.ADMIN_USERNAME and password == settings.ADMIN_PASSWORD:
        print(f"{settings.COLOR_GREEN}Login successful!{settings.COLOR_END}")
        time.sleep(1)
        admin_menu()
    else:
        print(f"{settings.COLOR_RED}Login Failed. Exiting.{settings.COLOR_END}")
        time.sleep(2)
        sys.exit()

def admin_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{settings.COLOR_YELLOW}--- MASAN ADMIN PANEL ---{settings.COLOR_END}")
        print("[1] View Active Targets")
        print("[2] Manage Proxies")
        print("[3] Enable/Disable Modules")
        print("[4] Toolkit Settings")
        print("[0] Exit Admin Panel")
        
        choice = input("\nSelect an Option: ")

        if choice == "1":
            view_targets()
        elif choice == "2":
            manage_proxies()
        elif choice == "3":
            manage_modules()
        elif choice == "4":
            toolkit_settings()
        elif choice == "0":
            break
        else:
            print("Invalid option. Try again!")

def view_targets():
    print(f"{settings.COLOR_GREEN}\nActive Targets:\n{settings.COLOR_END}")
    try:
        with open("data/targets.txt", "r") as f:
            targets = f.read()
            print(targets if targets else "No targets found.")
    except FileNotFoundError:
        print("No targets file found.")
    input("\nPress Enter to return...")

def manage_proxies():
    print(f"{settings.COLOR_GREEN}\nManaging Proxies:\n{settings.COLOR_END}")
    try:
        with open("data/proxies.txt", "r") as f:
            proxies = f.read()
            print(proxies if proxies else "No proxies found.")
    except FileNotFoundError:
        print("No proxies file found.")
    input("\nPress Enter to return...")

def manage_modules():
    print(f"{settings.COLOR_GREEN}\nEnable/Disable Modules (Coming Soon){settings.COLOR_END}")
    input("\nPress Enter to return...")

def toolkit_settings():
    print(f"{settings.COLOR_GREEN}\nToolkit Settings (Coming Soon){settings.COLOR_END}")
    input("\nPress Enter to return...")

if __name__ == "__main__":
    login()
