import hashlib

# List of weak passwords to generate hashes for
weak_passwords = ["password123", "letmein", "123456"]

# Open a file to save the hashes
with open("hashes.txt", "w") as file:
    for pwd in weak_passwords:
        hash_md5 = hashlib.md5(pwd.encode()).hexdigest()
        file.write(hash_md5 + "\n")

print("Hashes have been saved to hashes.txt")

