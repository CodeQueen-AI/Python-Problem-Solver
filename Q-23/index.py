#Take a password as input and check if it’s Weak, Medium or Strong
import re

password = input("Enter your password: ")

if len(password) < 6:
    print("Weak password")
elif 6 <= len(password) <= 10:
    print("Medium password")
elif re.search(r"\d", password) and re.search(r"[!@#$%^&*]", password):
    print("Strong password")
else:
    print("Medium password")
