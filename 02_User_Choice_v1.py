# Functions go here
def choice_checker(question):
    error = "Please choose from rock / paper / " \
            "scissors (or xxx to quit)"
    valid = False
    while not valid:

        # Ask user for choice
        response = input(question).lower()

        if response == "r" or response == "rock":
            return response
        elif response == "p" or response == "paper":
            return response
        elif response == "s" or response == "scissors":
            return response

        # Check for exit code...
        elif response == "xxx":
            return response
        else:
            print(error)


# Main Routine Goes Here

# Loop for test purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper /"
                                 "scissors (r/p/s: ")

    # Print out choice for comparison purposes
    print("you chose {}".format(user_choice))