# Game number 3
import requests

#open_exchange_rates_api:
MY_API_VALUE = "95b39d7977f9477f84b43da0ee00d428"

from score import add_score


def get_money_interval(difficulty):
    # Ensure difficulty is an integer
    difficulty = int(difficulty)
    base_url = "https://open.er-api.com/v6/latest/USD"
    params = {"apikey": MY_API_VALUE}
    nis = 10
    acceptable_diff = nis - difficulty
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            exchange_current_rate = data["rates"]["ILS"]
            return exchange_current_rate, acceptable_diff
        else:
            print("Error:", data["error"])
            return None

    except Exception as e:
        print("Error:", e)
        return None


def get_guess_from_user():
    # ask for a user guess
    while True:
        guess_user = input("\nPlease guess the value of USD converted to ILS (between 1 to 100):")
        # Ensure the guess number is an integer:
        if guess_user.isdigit():
            guess_user = int(guess_user)
            if guess_user in range(1, 100):
                return guess_user
            else:
                print("\nNOT in range! \n")
        else:
            print("\nInvalid input! Please enter a number.\n")


def compare_results(difficulty):
    # Ensure difficulty is an integer
    difficulty = int(difficulty)
    # call func 1:
    rate_diff = get_money_interval(difficulty)
    print("\nThis is the allowed difference you can have:", rate_diff[1])
    # call func 2:
    guess_user = get_guess_from_user()

    print("\nok, so this is the current rate of USD:", rate_diff[0])

    # compare
    # abs() function returns the absolute value of a number
    if abs(guess_user-rate_diff[0]) <= rate_diff[1]:
        print("your guess minus current rate of USD is:", guess_user-rate_diff[0])
        return True
    else:
        print("your guess minus current rate of USD is:", guess_user-rate_diff[0])
        print("it's more then the allowed difference :(")
        return False


def play(difficulty):
    # Ensure difficulty is an integer
    difficulty = int(difficulty)
    print(f"\nStarting Currency Roulette with difficulty level {difficulty}:")
    # we will call the compare, 1+2 already there
    result = compare_results(difficulty)
    if result:
        print("\nWINNER !!!!!")
        add_score(difficulty)
    else:
        print("\nLoser!")
