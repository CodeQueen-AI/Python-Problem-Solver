#Write a program that takes N numbers as input and counts how many are positive and how many are negative
n = int(input("Enter the number of elements: "))

positive_count = 0
negative_count = 0

for _ in range(n):
    num = int(input("Enter a number: "))
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print(f"Positive Numbers: {positive_count}")
print(f"Negative Numbers: {negative_count}")
