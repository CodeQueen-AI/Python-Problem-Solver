#Write a Python program that takes a number from the user and calculates the sum from 1 to that number
num = int(input("Enter Any Number:"))
total = sum(range(1, num + 1)) 

print('Result is: \n')
print(f'Sum is: {total}')
