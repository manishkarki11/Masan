# dashboard.py
import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import settings

# Colors & Theme
BG_COLOR = "#0D0D0D"
BTN_COLOR = "#8B0000"
TEXT_COLOR = "#FFFFFF"
HIGHLIGHT_COLOR = "#FF0000"

# Main Functions Mapping
tools = {
    "Website Scanner": "toolkit_files/core/modules/website_scanner.py",
    "DDoS Attack": "toolkit_files/core/modules/ddos.py",
    "Mass Deface": "toolkit_files/core/modules/mass_deface.py",
    "IP Grabber": "toolkit_files/core/modules/ip_grabber.py",
    "Auto Exploit": "toolkit_files/core/modules/auto_exploit.py",
    "Proxy Scraper": "toolkit_files/core/modules/proxy_scraper.py",
    "Reverse Shell": "toolkit_files/core/modules/reverse_shell.py",
    "Vuln Scanner": "toolkit_files/core/modules/vuln_scanner.py"
}

def run_tool(path):
    try:
        subprocess.Popen(["python", path])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start tool:\n{e}")

def create_main_window():
    root = tk.Tk()
    root.title("MASAN Control Center")
    root.geometry("1000x600")
    root.configure(bg=BG_COLOR)

    # Top Banner
    banner = tk.Label(root, text="MASAN CONTROL CENTER", font=("Consolas", 24, "bold"), fg=HIGHLIGHT_COLOR, bg=BG_COLOR)
    banner.pack(pady=20)

    # Sidebar with Buttons
    sidebar = tk.Frame(root, bg=BG_COLOR)
    sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=20)

    for tool_name, path in tools.items():
        btn = tk.Button(sidebar, text=tool_name, font=("Consolas", 14),
                        fg=TEXT_COLOR, bg=BTN_COLOR, activebackground=HIGHLIGHT_COLOR,
                        command=lambda p=path: run_tool(p))
        btn.pack(pady=8, fill="x")

    # Main Display Window
    main_area = tk.Frame(root, bg="#1A1A1A")
    main_area.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=20, pady=20)

    welcome_text = tk.Label(main_area, text="Welcome, MASAN!\n\nSelect a tool from the sidebar.",
                            font=("Consolas", 18), fg=TEXT_COLOR, bg="#1A1A1A")
    welcome_text.pack(expand=True)

    # Footer
    footer = tk.Label(root, text="MASAN TOOLKIT v1.0 | github.com/masan", fg=HIGHLIGHT_COLOR, bg=BG_COLOR, font=("Consolas", 10))
    footer.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
