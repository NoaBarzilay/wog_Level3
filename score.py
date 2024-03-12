# A package that is in charge of managing the scores file.
import os

SCORES_FILE = "scores.txt"


def points_of_winning(difficulty):
    return (difficulty * 3) + 5


def add_score(difficulty):
    try:
        # Try to read the current score from the scores file
        with open(SCORES_FILE, 'r') as file:
            current_score = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        # If the file is not found or cannot be read --> create a new file with a score of 0
        current_score = 0
        with open(SCORES_FILE, 'w') as file:
            file.write(str(current_score))

    # Calculate the new score based on the given difficulty
    new_score = current_score + points_of_winning(difficulty)

    # Write the new score to the file
    with open(SCORES_FILE, 'w') as file:
        file.write(str(new_score))

    # Print the updated score
    print(f"\nYour updated Score is : {new_score} ! :-)")


def read_score():
    try:
        with open(SCORES_FILE, 'r') as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError) as e:
        return f"ERROR {str(e)}"
