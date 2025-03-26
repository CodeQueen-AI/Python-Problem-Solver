#Take a string as input and check whether it is a palindrome or not (e.g., madam, level)
text = input("Enter a word: ")
print("Palindrome" if text == text[::-1] else "Not Palindrome")
