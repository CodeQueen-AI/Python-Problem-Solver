#Take a string as input and count the number of vowels (a, e, i, o, u)
text = input("Enter a string: ").lower()
count = 0

for char in text:
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)
