# Game number 1
import random
import time
import os
import requests

from utils import screen_cleaner
from score import add_score


def generate_sequence(difficulty):
    # Ensure difficulty is an integer
    difficulty = int(difficulty)
    # Generate list of $diff random numbers between 1 and 101
    random_list = random.sample(range(1, 101), difficulty)
    return random_list


def get_list_from_user(difficulty):
    # Ensure difficulty is an integer
    difficulty = int(difficulty)
    # Create empty list
    user_list = []
    # keep prompting the user until the length is difficulty
    while len(user_list) < difficulty:
        print("Please enter number to list:")
        number = input()
        if number.isdigit():
            number = int(number)
            if number in range(1, 101):
                user_list.append(number)
            else:
                print("\nNOT in range! Please enter a right number.\n")
        else:
            print("\nInvalid input! Please enter a number.\n")
    return user_list


def is_list_equal(difficulty):
    # Ensure difficulty is an integer
    difficulty = int(difficulty)
    # call functions 1 + 2 :
    random_list = generate_sequence(difficulty)
    print("\n\nthis is the random list:", random_list)
    # Pause for 0.7 seconds
    time.sleep(0.7)
    # clear
    screen_cleaner()
    guess_list = get_list_from_user(difficulty)
    print("\n\nthis is your guess list:", guess_list)
    print("this is the random list:", random_list)
    if random_list == guess_list:
        return True
    else:
        return False


def play(difficulty):
    # Ensure difficulty is an integer
    difficulty = int(difficulty)
    print(f"\nStarting Memory Game with difficulty level {difficulty}:")
    # Pause for 2 seconds
    time.sleep(2)
    # call the compare func, 1 + 2 already there
    result = is_list_equal(difficulty)
    if result:
        print("\nWINNER !!!!!")
        add_score(difficulty)
    else:
        print("\nLoser!")
