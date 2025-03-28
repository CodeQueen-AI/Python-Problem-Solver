#Take an email as input and check if it’s valid (must have "@" and ".") or fake
email = input("Enter your email: ")

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Fake email")
