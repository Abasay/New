import random

# Using constants

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5

def set_difficulty(difficult):
    if difficult == 'easy':
        return EASY_DIFFICULTY
    else:
        return HARD_DIFFICULTY


print("Welcome to the number Guessing Game!\nI'm thinking of a number between 1 and 100, Guess the number.")

rand_number = random.randint(1, 100)

difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")

attempts = set_difficulty(difficulty)
while attempts != 0:
    print(f"You have {attempts} attempts left to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == rand_number:
        print(f"You got it! The answer is {rand_number}")
        break
    elif guess < rand_number:
        print("Too low.\nGuess again.")
    elif guess > rand_number:
        print("Too high.\nGuess again.")
    attempts -= 1

if attempts == 0:
    print("You lose!")