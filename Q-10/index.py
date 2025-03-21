#Find the square root
#Solution1 - Using Exponentiation
num1 = 64
num2 = int(input('Enter a Number Here:'))
sr = num2**(0.5)
print('The square root of the given number is' , sr)

#Solution2 - using Module
import math
num = int(input('enter a number here:'))
sr = math.sqrt(num)
print('the square root of the given number' , sr)


