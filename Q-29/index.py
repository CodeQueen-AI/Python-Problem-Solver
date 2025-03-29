#Write a program that calculates the sum of digits of a given number
# Take input from user
num = int(input("Enter a number: "))

sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num = num // 10 

print(f"Sum of digits: {sum_digits}")
