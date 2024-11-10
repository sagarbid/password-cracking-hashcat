# Password Cracking Project Using Hashcat

## Overview
This project demonstrates how to crack password hashes using Hashcat, emphasizing the importance of password security.

## Steps
- Setup environment on macOS.
- Generate sample hashes using Python.
- Run dictionary attacks with Hashcat.
- Analyze the results and recommend mitigation strategies.

## Requirements
- Hashcat
- Python 3
- Wordlist (e.g., rockyou.txt)

## Usage
1. Generate password hashes using `generate_hashes.py`.
2. Run Hashcat with `hashcat -m 0 -a 0 hashes.txt rockyou.txt`.
3. Analyze the cracked passwords for security insights.

