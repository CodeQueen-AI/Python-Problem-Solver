#Calculate the factorial of a given number (e.g., 5! = 5 × 4 × 3 × 2 × 1)
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)
