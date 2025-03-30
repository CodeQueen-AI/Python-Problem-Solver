#Write a program that checks if a given string is a palindrome (reads the same forward and backward)
text = input("Enter a string: ").lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
