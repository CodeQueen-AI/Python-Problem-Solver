#Write a program that takes a number as input and prints its reverse
num = int(input("Enter a number: "))

reverse_num = 0
while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10

print(f"Reversed number: {reverse_num}")
