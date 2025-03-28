#The program picks a random number between 1-100. The user has to guess it!
import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (1-100): "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it!")
        break
