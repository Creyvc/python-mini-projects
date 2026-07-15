import random

print("Welcome to the Number Guessing Game.")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"You have 10 chances to guess the number between {low} and {high}. Let's start!")

number = random.randint(low, high)
chances = 10
guess_count = 0

while guess_count < chances:
    guess_count += 1
    guess = int(input("Enter your guess: "))

    if guess == number:
        print(f"Correct! The number is {number}. You guessed it in {guess_count} attempts.")
        break

    elif guess_count >= chances and guess != number:
        print(f"Sorry! The number was {number}. Try again next time.")

    elif guess > number:
        print("Too high! Try a lower number.")

    elif guess < number:
        print("Too low! Try a higher number.")
#1