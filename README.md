# HrskiEsa Tool - Pentesting Automation Script

## Description
HrskiEsa is an automated pentesting script designed to streamline common security testing tasks. It provides an easy-to-use interface for installing, running security tools, and downloading useful wordlists.

## Features
- Install and run popular pentesting tools
- Choose and download wordlists from a public GitHub repository
- Simple command-line interface for ease of use

## Installation
### Prerequisites
- Linux-based OS (Ubuntu, Kali Linux, Parrot OS, etc.)
- Python 3 installed

### Install Required Dependencies
```bash
sudo apt update && sudo apt install -y python3 python3-pip
pip install requests
```

### Clone the Repository
```bash
git clone https://github.com/yourrepo/HrskiEsa-Tool
cd HrskiEsa-Tool
```

### Run the Script
```bash
chmod +x hrskiesa_tool.py
./hrskiesa_tool.py
```

## Usage
1. Install all tools: Select option `1`
2. Run a specific tool: Select option `2`
3. Choose and download a wordlist: Select option `3`
4. Show help menu: Select option `4`
5. Exit: Select option `5`

## Contributing
Feel free to submit pull requests to improve or expand the script.

## License
This project is licensed under the MIT License.

