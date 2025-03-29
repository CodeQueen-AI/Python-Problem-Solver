#Write a program that gives a random funny life prediction when the user enters their name
import random

fortunes = [
    "You will eat too much pizza today! 🍕",
    "Your crush is thinking about you! ❤️",
    "You will find money on the ground soon! 💰",
    "You will have a lucky day today! 🍀",
    "Be careful, someone is watching you! 👀"
]

name = input("Enter your name: ")
print(name + ", your fortune is: " + random.choice(fortunes))
