# Python Menu Program (CLI)

A simple Python command-line menu application built for university coursework to practise programming fundamentals and basic automation tasks.

## Features
- Display date and time
- Show local IP/network information
- Run basic remote tasks (via SSH) using Netmiko (optional)
- Create a simple backup of selected files/folders (local)
- Fetch and save a webpage to a file (Requests)

## Project Structure

Python-Menu-Program/
├─ src/
│ └─ menu_program.py
├─ README.md
├─ requirements.txt
└─ .gitignore


## Quickstart
Clone the repository and install dependencies:

```bash
git clone https://github.com/KainaCardoso/Python-Menu-Program.git
cd Python-Menu-Program
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 src/menu_program.py
