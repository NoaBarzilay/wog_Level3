# Game number 2
import random

from score import add_score


def generate_number(difficulty):
    # Ensure difficulty is an integer
    difficulty = int(difficulty)
    # Use random.randint to generate a random number between 0 and difficulty
    secret_number = random.randint(0, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    # Ensure difficulty is an integer
    difficulty = int(difficulty)
    # ask for a user guess
    while True:
        guess_user = input("\nplease enter your guess number here --> \nit must to be in range of 0 to your chosen "
                           "diff level.\n")
        # Ensure the guess number is an integer:
        if guess_user.isdigit():
            guess_user = int(guess_user)
            if guess_user in range(0, difficulty+1):
                return guess_user
            else:
                print("\nNOT in range! \n")
        else:
            print("\nInvalid input! Please enter a number.\n")


def compare_results(difficulty):
    # Ensure difficulty is an integer
    difficulty = int(difficulty)
    # 1 + 2 :
    secret_number = generate_number(difficulty)
    guess_user = get_guess_from_user(difficulty)
    print("\nthis is your guess number:", guess_user)
    print("this is the secret_number:", secret_number)
    if secret_number == guess_user:
        return True
    else:
        return False


def play(difficulty):
    # Ensure difficulty is an integer
    difficulty = int(difficulty)
    print(f"\nStarting Guess Game with difficulty level {difficulty}:")
    # we will call the compare, 1+2 already there
    result = compare_results(difficulty)
    if result:
        print("\nWINNER !!!!!")
        add_score(difficulty)
    else:
        print("\nLoser!")
