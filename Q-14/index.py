#Take a number as input and check whether it is prime or not
num = int(input("Enter a number: "))
is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
print("Prime" if is_prime else "Not Prime")
