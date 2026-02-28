# 🔐 Password Cracking with Hashcat

> **Cybersecurity project demonstrating brute-force and dictionary-based password attacks using Hashcat, automated with Python and Bash scripting.**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Bash](https://img.shields.io/badge/Bash-Scripting-green?style=flat-square&logo=gnubash)
![Hashcat](https://img.shields.io/badge/Tool-Hashcat-red?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-purple?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

---

## 📌 Project Overview

This project was completed as part of the **Monash University Cybersecurity Bootcamp (2024)** and presented at the bootcamp's final conference. It demonstrates the practical mechanics of password cracking using Hashcat — one of the most widely used tools in both offensive security and blue team password auditing workflows.

The project highlights how weak passwords can be compromised rapidly using automated tooling, and why strong password policies and hashing algorithms matter in real-world systems.

---

## 🎯 Objectives

- Demonstrate brute-force and dictionary attacks against hashed password files
- Automate repetitive cracking tasks using Python and Bash scripts
- Understand and compare hash algorithm strength (MD5, SHA-1, bcrypt)
- Communicate security implications to a non-technical audience

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Hashcat | Password hash cracking engine |
| Python 3 | Automation scripting |
| Bash | Shell scripting for task orchestration |
| Kali Linux | Attack platform |
| RockYou wordlist | Dictionary attack source |

---

## 🔬 Methodology

### 1. Hash Generation
Created sample password hash files using MD5, SHA-1, and bcrypt to simulate real-world credential leaks.

### 2. Dictionary Attack
Used Hashcat with the RockYou wordlist to crack MD5 and SHA-1 hashes, demonstrating how quickly common passwords are compromised.

```bash
hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt
```

### 3. Brute-Force Attack
Configured mask attacks to systematically crack short passwords of known character sets.

```bash
hashcat -m 0 -a 3 hashes.txt ?a?a?a?a?a?a
```

### 4. Python Automation
Wrote a Python script to automate hash generation, attack execution, and result logging for batch processing.

### 5. Results Analysis
Compared crack rates across hash types — demonstrating bcrypt's resistance vs MD5's vulnerability.

---

## 📊 Key Findings

- **MD5 hashes** for common passwords cracked in under 2 seconds
- **SHA-1** similarly vulnerable to dictionary attacks
- **bcrypt** with cost factor 12 showed significant resistance, demonstrating the importance of algorithm selection
- 68% of test passwords cracked within 10 minutes using dictionary attack alone

---

## 🔐 Security Implications

This project reinforces why organisations must enforce:
- Minimum password length and complexity requirements
- Use of strong, slow hashing algorithms (bcrypt, Argon2, scrypt)
- Multi-factor authentication as a compensating control
- Regular credential auditing using tools like this in controlled environments

---

## ⚠️ Legal & Ethical Disclaimer

This project was conducted in a controlled, isolated lab environment for **educational purposes only** as part of an accredited cybersecurity bootcamp. Password cracking against systems without explicit written authorisation is illegal. All techniques demonstrated here should only be applied in authorised penetration testing or security auditing contexts.

---

## 👤 Author

**Sagar Bidari**
CompTIA Security+ CE | Monash University Cybersecurity Bootcamp Graduate
🌐 [bidarisagar.com](https://bidarisagar.com) | 💼 [LinkedIn](https://linkedin.com/in/sagarbidari)
