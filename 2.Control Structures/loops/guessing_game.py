#Write a Python program to simulate a number guessing game where the program generates a random number, and the user has to guess it.

import random

n=random.randint(1,10)

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100. Can you guess it?")

while True:
    guess= int(input("Enter the guess : "))
    
    if guess < n:
        print("Too low! Try again.")
    elif guess > n:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the correct number: {n}")
        break