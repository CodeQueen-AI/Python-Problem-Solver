# Write a Python program that takes a number from the user and checks whether it is odd
num = int(input("Enter a Number: "))

if num % 2 != 0:
    print(f"{num} is an Odd number")
else:
    print(f"{num} is not an Odd number")