""" Necessary Modules:
- random: To generate a random number for the game."""

import random

# Function to play the number guessing game
# This is a simple number guessing game where the user has to guess a number between 1 and 10.
def number_guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    max_attempts = 3

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 10.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break
    else:
        print(f"Sorry! You've used all your attempts. The number was {number_to_guess}.")


def main():
    number_guessing_game()

if __name__ == "__main__":
    main()