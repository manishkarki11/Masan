# MASAN_TOOLKIT - MAIN.PY
# Made for MASAN - 2025

import os
import time
import sys
import threading

# ASCII Logo Banner
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_logo = r"""
███████╗██╗   ██╗███████╗ █████╗ ███╗   ██╗
██╔════╝██║   ██║██╔════╝██╔══██╗████╗  ██║
███████╗██║   ██║█████╗  ███████║██╔██╗ ██║
╚════██║██║   ██║██╔══╝  ██╔══██║██║╚██╗██║
███████║╚██████╔╝██║     ██║  ██║██║ ╚████║
╚══════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝
       MASAN TOOLKIT - 2025
    """
    print(f"\033[91m{ascii_logo}\033[0m")
    print("")

# Startup Music (optional)
def play_music():
    try:
        import playsound
        threading.Thread(target=playsound.playsound, args=('banner_music.mp3',), daemon=True).start()
    except Exception:
        pass  # Skip if module missing

# Menu
def menu():
    print("[1] Website Scanner")
    print("[2] DDoS Attack (Multi Vector)")
    print("[3] Multi-Target Attack Mode")
    print("[4] Cloudflare Bypass")
    print("[5] Mass Deface Attack")
    print("[6] Reverse Shell Generator")
    print("[7] Proxy Scraper")
    print("[8] Vulnerability Scanner")
    print("[9] Auto Exploit CMS")
    print("[10] IP Grabber Generator")
    print("[11] Admin Panel Finder")
    print("[12] Brute Force Attack")
    print("[13] Website Info Gathering")
    print("[14] SQL Injection Exploiter")
    print("[15] Port Scanner")
    print("[16] Hash Cracker")
    print("[17] File Upload Exploiter")
    print("[0] Exit Toolkit")

# Action Handler
def run_tool(choice):
    if choice == '1':
        os.system('python modules/website_scanner.py')
    elif choice == '2':
        os.system('python modules/ddos_attack.py')
    elif choice == '3':
        os.system('python modules/multi_target_ddos.py')
    elif choice == '4':
        os.system('python modules/cloudflare_bypass.py')
    elif choice == '5':
        os.system('python modules/mass_deface.py')
    elif choice == '6':
        os.system('python modules/reverse_shell.py')
    elif choice == '7':
        os.system('python modules/proxy_scraper.py')
    elif choice == '8':
        os.system('python modules/vuln_scanner.py')
    elif choice == '9':
        os.system('python modules/auto_exploit.py')
    elif choice == '10':
        os.system('python modules/ip_grabber.py')
    elif choice == '11':
        os.system('python modules/admin_finder.py')
    elif choice == '12':
        os.system('python modules/brute_force.py')
    elif choice == '13':
        os.system('python modules/website_info.py')
    elif choice == '14':
        os.system('python modules/sql_injector.py')
    elif choice == '15':
        os.system('python modules/port_scanner.py')
    elif choice == '16':
        os.system('python modules/hash_cracker.py')
    elif choice == '17':
        os.system('python modules/upload_exploit.py')
    elif choice == '0':
        print("Exiting MASAN Toolkit... Goodbye!")
        sys.exit()
    else:
        print("\nInvalid Option. Try Again.\n")
        time.sleep(2)

# MAIN PROGRAM
def main():
    banner()
    play_music()
    while True:
        menu()
        choice = input("\nMASAN > Enter Option Number: ")
        run_tool(choice)
        print("\nReturning to MASAN menu...\n")
        time.sleep(1)
        banner()

if __name__ == "__main__":
    main()
