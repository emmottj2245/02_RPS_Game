# RPS component 6 - scoring system

# Rounds won will be calculated (total - draw - lost)
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# results for testing purposes
test_results = ["won", "won", "loss", "loss", "tie"]

# play game
for item in test_results:
    rounds_played += 1

    # generate computer choice

    result = item

    if result == "tie":
        result = "its a tie"
        rounds_drawn += 1
    elif result == "loss":
        rounds_lost += 1

# quick calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# end games statements
print()
print('***** End Game Summary *****')
print("won: {} \t|\t Lost: {} \t|t\t Draw: "
      "{}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thank you for playing")
