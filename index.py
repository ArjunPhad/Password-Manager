import random
   
import string

passwords = {}

#load existing passwords from file
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, password = line.strip().split(":")
    passwords[website] = password
except:
    pass

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-+"
    password = "".join(random.choice(chars) for _ in range(length))
    return password

while True:
    print("\n--- Password Manager ---")
    print("1. Generate Password")
    print("2. Save Password")
    print("3. Retrieve Password")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        site = input("Enter the website: ")
        password = generate_password()
        print(f"Generated password for {site}: {password}")
    elif choice == "2":
        site = input("Enter the website: ")
        password = input("Enter your password: ")
        passwords[site] = password
        with open("passwords.txt", "a") as file:
            file.write(f"{site}:{password}\n")
        print("Password saved successfully.")
    elif choice == "3": 
        site = input("Enter the website: ")
        if site in passwords:
            print(f"Password for {site}: {passwords[site]}")
        else:
            print("No password found for this website.")
    elif choice == "4":
        print("Exiting Password Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")