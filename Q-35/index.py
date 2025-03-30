#Write a program that takes a number as input and calculates the sum of its digits
num = int(input("Enter a Number: "))

sum_digits = 0

while num > 0:
    sum_digits += num % 10  
    num //= 10 

print(f"Sum of digits: {sum_digits}")
