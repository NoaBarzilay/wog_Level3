# Noa Barzilay - course 1312
import webbrowser
import games.currency_roulette_game
import games.guess_game
import games.memory_game


def welcome():
    while True:
        user_name = input("Hi you! What is your name? ")
        if isinstance(user_name, str) and user_name.isalpha():
            print("\nHi", user_name, "and welcome to the World of Games: The Epic Journey!")
            break
        else:
            print("\nInvalid input! please try again.\n")


def get_input(value, validate_func):
    while True:
        user_input = input(value)
        if validate_func(user_input):
            return int(user_input)
        else:
            print("\nInvalid input! Please try again.\n")


def games_info():
    print("\nPlease choose a game to play: \n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have "
          "to guess it back.\n"
          "2. Guess Game - guess a number and see if you chose like the computer. \n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n")


def start_play():
    games_info()
    games_dir = {1: "Memory Game", 2: "Guess Game", 3: "Currency Roulette"}

    while True:
        game_number = get_input("Your game choice is: ", lambda x: x.isdigit() and int(x) in games_dir)
        print(game_number, "is a nice choice! :)")
        diff_level = get_input("Please select a difficulty level between 1 and 5: ",
                               lambda x: x.isdigit() and int(x) in range(1, 6))
        print(f"{diff_level} - this is a good one! ;)")

        # Execute the selected game function
        if game_number == 1:
            games.memory_game.play(diff_level)
        elif game_number == 2:
            games.guess_game.play(diff_level)
        else:
            games.currency_roulette_game.play(diff_level)

        # Check if the user wants to keep playing games:
        play_again = input("\nDo you want to play again? (yes/no): \n").lower()
        if play_again != 'yes':
            # Open the Flask app URL with the score of all games
            flask_url = f'http://127.0.0.1:5003'
            webbrowser.open(flask_url)

            # Exit the game loop
            break

        # If the user wants to play again, show game options
        games_info()










# def start_play():
#     print("\nPlease choose a game to play: \n"
#           "1. Memory Game - a sequence of numbers will appear for 1 second and you have "
#           "to guess it back.\n"
#           "2. Guess Game - guess a number and see if you chose like the computer. \n"
#           "3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n")
#     while True:
#         game_number = input("Your game choice is: ")
#         if game_number.isdigit():
#             game_number = int(game_number)
#             if game_number in [1, 2, 3]:
#                 #print(game_number, "is a nice choice! :)")
#                 while True:
#                     diff_level = input("Please select a difficulty level between 1 and 5: ")
#                     if diff_level.isdigit():
#                         diff_level = int(diff_level)
#                         if diff_level in range(1, 6):
#                             print(diff_level, "- this is a good one! ;)")
#                             # 1 = Memory Game:
#                             if game_number == 1:
#                                 play_1(diff_level)
#                             break
#                         else:
#                             print("\nNOT in range! \n")
#                     is_empty_or_invalid(diff_level)
#                 break
#             else:
#                 print("\nNOT in range! \n")
#         is_empty_or_invalid(game_number)


# def is_empty_or_invalid(value):
#     if value == "":
#         print("No input provided! Please enter something.")
#     else:
#         print("This is invalid value! Please enter your value again.")
