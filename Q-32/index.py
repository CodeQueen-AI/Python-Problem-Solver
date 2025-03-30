#Write a program that takes a list of numbers as input and finds the largest and smallest numbers in the list
n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)

print(f"Largest Number: {largest}")
print(f"Smallest Number: {smallest}")
