# RPS component 3 - Compare user choice and compare choice
from unittest import result

rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_choice]
        user_index += 1

        print("you choose {}, the computer choice {}. "
              "\nResult: {}".format(user_choice, comp_choice, result))

    comp_index += 1
    print()