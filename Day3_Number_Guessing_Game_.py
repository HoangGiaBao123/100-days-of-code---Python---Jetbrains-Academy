# Guess the random number game
import random

max_num = int(input("Guess a number from 1 to: "))
random_num = random.randint(1, max_num)

print(f"Ok, let's guess ab number from 1 to {max_num}")

while True:
    guess = int(input("Enter a number here: "))

    if guess > random_num:
        print("Too high! Try again!")
    elif guess < random_num:
        print("Too low! Try again!")
    else:
        print("Yes, it is! You won this game!")
        break
