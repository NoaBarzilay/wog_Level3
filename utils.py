# A general purpose python file - general information and operations
import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 0


def screen_cleaner():
    # Check the operating system and use the appropriate command to clear the screen
    if os.name == 'posix':  # For UNIX/Linux/MacOS
        os.system('clear')
    else:
        # If the operating system is not recognized, simply print 50 newlines to simulate clearing the screen
        print('\n' * 50)
