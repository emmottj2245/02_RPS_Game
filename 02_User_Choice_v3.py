# Version 3 - error message included when calling function


# Functions go here
def choice_checker(question, error, valid_list):

    while True:

        # Ask user for choice
        response = input(question).lower()

        for item in valid_list:
            if response == item or response == item[0]:
                return item

        print(error)


# Main Routine Goes Here

rps_list = ["rock", "paper", "scissors", "xxx"]
yes_no_list = ["yes", "no"]

want_instructions = choice_checker("Do you want to see the instructions? ",
                                   "Please enter yes / no",
                                   yes_no_list)

# Loop for test purposes
user_choice = ""
while user_choice != "xxx":
    
    # Ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ",
                                 "Please choose from rock / paper / scissors (or xxx to quit)",
                                 rps_list
                                 )

    # Print out choice for comparison purposes
    print("you chose {}".format(user_choice))
