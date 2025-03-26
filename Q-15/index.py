#Print the first n Fibonacci numbers (e.g., 0, 1, 1, 2, 3, 5, 8, ...)
n = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
