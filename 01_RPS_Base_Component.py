import random


# function go here
def check_rounds():
    while True:
        response = input("how many rounds: ")

        round_error = "Please type either <enter> " \
                      " or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here

# list of valid responses
yes_no_list = ["yes, no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before
# If 'yes', show instructions

# Ask user  for # of round then loop...

# Ask user if they want to see their game history.
# If 'yes' show game history

# show game statistics
