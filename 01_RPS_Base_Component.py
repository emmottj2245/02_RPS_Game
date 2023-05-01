import random


# function go here
# Checks users enter a valid response based on a list
# accepts first letter / full word and returns full word
def choice_checker(question, valid_list, error):
    while True:

        # Ask user for choice
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)


# checks users enter an integer more than zero.
# Accepts <enter> (infinite mode)
def check_rounds():
    while True:
        response = input("how many rounds: ")

        round_error = "Please type either <enter> " \
                      " or an integer that is more than 0\n"
        # If infinite
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


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no")


def instructions():
    print("***** How to play *****")
    print()
    print("it's a simple game of rock, paper, scissors")
    print()
    print("you should know how to play")
    return ""


# main routine goes here...
played_before = yes_no("have you played this game"
                       " before? ")

if played_before == "no":
    instructions()

print("press <enter> to play infinite mode")
print()

# Main routine goes here

# list of valid responses
yes_no_list = ["yes, no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before
# If 'yes', show instructions

# Ask user  for # of round then loop...
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Generate Heading depending on mode
    print()
    if rounds == "":
        heading = "Continuous Mode: " \
                  "Round {}".format(rounds_played + 1)
    else:
        heading = "round {} of " \
                  "{}".format(rounds_played + 1, rounds)

    # print round heading and ask user for choice
    print(heading)
    choose_instruction = "Please choose rock (r), paper " \
                         "(p) or scissors (s)" \
                         "or 'xxx' to exit: "
    choose_error = "Please choose from rock / " \
                   "paper / scissors (or xxx to quit)"

    # Ask user for choice and check it's valid
    user_choice = choice_checker(choose_instruction, rps_list,
                                 choose_error)

    # end  game if exit code is typed
    if user_choice == "xxx":
        break

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])

    # compare choices
    if comp_choice == user_choice:
        result = "tie"
        rounds_drawn += 1
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "won"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "won"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "won"
    else:
        result = "lost"
        rounds_lost += 1

    if result == "tie":
        feedback = "It's a tie"
        print(f'you chose: {user_choice}')
        print(f'computer chose: {comp_choice}')
    else:
        feedback = f'{user_choice} vs {comp_choice} = {result}'

    # Rest of the loop / Game
    print(feedback)

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Ask user if they want to see their game history.
# If 'yes' show game history

# show game statistics
# quick calculations (stats)
game_summary = []

if rounds_played > 0:
    rounds_won = rounds_played - rounds_lost - rounds_drawn

    # **** Calculate Game Stats
    percent_win = rounds_won / rounds_played * 100
    percent_lose = rounds_lost / rounds_played * 100
    percent_tie = rounds_drawn / rounds_played * 100

    print()
    print("***** Game History *****")
    for game in game_summary:
        print(game)

    print()

    # displays game stats with : values to the nearest whole number
    print("******* Game Statistics *******")
    print("win: {}, ({:.0f}%)\nLoss: {}, "
          "({:.0f}%)\nTie: {}, ({:.0f}%)".format(rounds_won,
                                                 percent_win,
                                                 rounds_lost,
                                                 percent_lose,
                                                 rounds_drawn,
                                                 percent_tie))
    # end games statements
    print()
    print('***** End Game Summary *****')
    print(f"won: {rounds_won} \t|\t Lost: {rounds_lost} \t|t\t Draw: {rounds_drawn}")
    print()
    print("Thank you for playing")
else:
    print()
    print("you must be afraid young padawan")
