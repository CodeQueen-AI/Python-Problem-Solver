##Write a program that takes N numbers as input and calculates the sum of even and odd numbers separately
n = input("Enter the number of elements: ").strip()

if n.isdigit():
    n = int(n)
else:
    print("Invalid input! Please enter a valid number.")
    exit()

even_sum = 0
odd_sum = 0

for _ in range(n):
    num_str = input("Enter a number: ").strip()

    if num_str.isdigit() or (num_str.startswith('-') and num_str[1:].isdigit()):
        num = int(num_str)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    else:
        print("Invalid input! Please enter a valid number.")
        exit()

print(f"Sum of Even Numbers: {even_sum}")
print(f"Sum of Odd Numbers: {odd_sum}")
