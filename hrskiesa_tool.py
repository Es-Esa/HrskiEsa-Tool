#!/usr/bin/env python3

import os
import sys
import subprocess
import webbrowser
from time import sleep

# ASCII Art Logo
LOGO = """
  _  _ ___  ___ _  _____ ___ ___   _     _____ ___   ___  _    
 | || | _ \\/ __| |/ /_ _| __/ __| /_\\   |_   _/ _ \\ / _ \\| |   
 | __ |   /\\__ \\ ' < | || _|\\__ \\/ _ \\    | || (_) | (_) | |__ 
 |_||_|_|_\\|___/_|\\_\\___|___|___/_/ \\_\\   |_| \\___/ \\___/|____|
"""

# Tool Descriptions
TOOLS = {
    "nmap": "Network scanner for discovery and security auditing.",
    "wireshark": "Network protocol analyzer for deep packet inspection.",
    "metasploit": "Exploitation framework for penetration testing.",
    "sqlmap": "Automatic SQL injection and database takeover tool.",
    "gobuster": "Directory/file busting tool for web applications.",
    "hydra": "Network login cracker for brute-forcing credentials.",
    "nikto": "Web server scanner for vulnerabilities.",
    "aircrack-ng": "Wireless network security tool suite.",
    "wfuzz": "Web application fuzzer for finding vulnerabilities.",
    "dirb": "Web content scanner for discovering hidden files.",
    "john": "Password cracker for offline password auditing.",
    "ffuf": "Fast web fuzzer for directory and parameter discovery.",
    "crackmapexec": "Swiss army knife for network penetration testing.",
    "bloodhound": "Active Directory relationship analysis tool.",
    "enum4linux": "Tool for enumerating information from Windows systems.",
    "smbmap": "SMB share enumeration and access tool.",
    "searchsploit": "Exploit database search tool.",
    "tcpdump": "Packet analyzer for network traffic capture.",
    "netcat": "Networking utility for reading/writing network connections.",
    "masscan": "Mass IP port scanner.",
    "whatweb": "Web application fingerprinting tool.",
}

# Check if a tool is installed
def is_tool_installed(tool):
    return subprocess.call(f"which {tool} > /dev/null 2>&1", shell=True) == 0

# Install a tool if not already installed
def install_tool(tool):
    if is_tool_installed(tool):
        print(f"[+] {tool} is already installed.")
    else:
        print(f"[*] Installing {tool}...")
        os.system(f"sudo apt install -y {tool}")

# Run a tool with user input
def run_tool(tool):
    if tool not in TOOLS:
        print(f"[-] {tool} is not supported.")
        return

    install_tool(tool)
    print(f"\n[+] Running {tool}...")

    if tool == "nmap":
        target = input("Enter target IP or domain: ")
        os.system(f"nmap -sV -sC {target}")

    elif tool == "sqlmap":
        url = input("Enter target URL: ")
        os.system(f"sqlmap -u {url} --batch")

    elif tool == "gobuster":
        url = input("Enter target URL: ")
        wordlist = input("Enter path to wordlist (default: /usr/share/wordlists/dirb/common.txt): ") or "/usr/share/wordlists/dirb/common.txt"
        os.system(f"gobuster dir -u {url} -w {wordlist}")

    elif tool == "hydra":
        target = input("Enter target IP or domain: ")
        service = input("Enter service (e.g., ssh, ftp): ")
        username = input("Enter username (or path to userlist): ")
        wordlist = input("Enter path to password wordlist: ")
        os.system(f"hydra -l {username} -P {wordlist} {target} {service}")

    elif tool == "nikto":
        target = input("Enter target URL: ")
        os.system(f"nikto -h {target}")

    elif tool == "john":
        hash_file = input("Enter path to hash file: ")
        os.system(f"john {hash_file}")

    elif tool == "tcpdump":
        interface = input("Enter network interface (e.g., eth0, wlan0): ")
        os.system(f"sudo tcpdump -i {interface} -n")

    elif tool == "masscan":
        target = input("Enter target IP range (e.g., 192.168.1.0/24): ")
        ports = input("Enter port range (e.g., 1-1000): ")
        os.system(f"sudo masscan -p{ports} {target}")

    elif tool == "whatweb":
        target = input("Enter target URL: ")
        os.system(f"whatweb {target}")

    else:
        print(f"[!] No automation for {tool} yet. Run it manually.")

# Open wordlist GitHub page
def open_wordlist_github():
    print(LOGO)
    print("[*] Opening wordlist GitHub page in your default browser...")
    webbrowser.open("https://github.com/kkrypt0nn/wordlists/tree/main/wordlists")
    print("[+] GitHub page opened. You can now browse and download wordlists.")

# Display help menu
def show_help():
    print(LOGO)
    print("HrskiEsa Tool - Pentesting Automation Script")
    print("\nUsage:")
    print("  1. Install all tools")
    print("  2. Run a specific tool")
    print("  3. Open wordlist GitHub page")
    print("  4. Show help menu")
    print("  5. Exit")
    print("\nSupported Tools:")
    for tool, desc in TOOLS.items():
        print(f"  {tool.ljust(20)} {desc}")

# Install all tools
def install_all_tools():
    print(LOGO)
    print("[*] Installing all tools...")
    for tool in TOOLS:
        install_tool(tool)
    print("[+] All tools installed!")

# Main menu loop
def main_menu():
    while True:
        print(LOGO)
        print("HrskiEsa Tool - Pentesting Automation Script")
        print("\nMain Menu:")
        print("  1. Install all tools")
        print("  2. Run a specific tool")
        print("  3. Open wordlist GitHub page")
        print("  4. Show help menu")
        print("  5. Exit")
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            install_all_tools()
        elif choice == "2":
            print("\nInstalled Tools:")
            installed_tools = [tool for tool in TOOLS if is_tool_installed(tool)]
            for tool in installed_tools:
                print(f"  [+] {tool} is installed.")
            if not installed_tools:
                print("[-] No tools are installed. Run option 1 first.")
            tool = input("\nEnter the tool name to run: ")
            run_tool(tool)
        elif choice == "3":
            open_wordlist_github()
        elif choice == "4":
            show_help()
        elif choice == "5":
            print("[+] Exiting HrskiEsa Tool. Goodbye!")
            break
        else:
            print("[-] Invalid choice. Please try again.")

        input("\nPress Enter to continue...")

# Main function
def main():
    main_menu()

if __name__ == "__main__":
    main()
