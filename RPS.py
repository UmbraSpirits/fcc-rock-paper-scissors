# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], my_history=[], won_games=[0], lost_games=[0],
           play_order=[{
               "RR": 0,
               "RP": 0,
               "RS": 0,
               "PR": 0,
               "PP": 0,
               "PS": 0,
               "SR": 0,
               "SP": 0,
               "SS": 0,
           }]):
    # Reset params if new player
    if prev_play != "":
        opponent_history.append(prev_play)
    else:
        print("reset")
        opponent_history.clear()
        my_history.clear()
        won_games.insert(0, 0)
        lost_games.insert(0, 0)

    responses = {'P': 'R', 'R': 'S', 'S': 'P'}

    amountOfGames = len(my_history)

    if amountOfGames > 0:
        # Count for games won
        if responses[my_history[-1]] == opponent_history[-1]:
            won_games.insert(0, won_games[0] + 1)
        # Count for games lost
        if my_history[-1] == responses[opponent_history[-1]]:
            lost_games.insert(0, lost_games[0] + 1)

        # Calculate winrate
        if won_games[0] > 0:
            winrate = (won_games[0] / (won_games[0] + lost_games[0])) * 100
        elif lost_games[0] > 0:
            winrate = 0
        else:
            winrate = 100

        if winrate == 100:
            # Counter Quincy start with him for 100 % win
            order = ["P", "S", "S", "R", "P"]
            count = (amountOfGames) % 5
            guess = order[count]
        elif amountOfGames <= 10 or winrate >= 87:
            # counter Kriss --> Start with him second for a bit less than 100% win
            ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
            guess = ideal_response[my_history[-1]]
        elif amountOfGames <= 20 or winrate > 82:
            # counter Mrugesh
            last_ten = my_history[-10:]
            most_frequent = max(set(last_ten), key=last_ten.count)

            if most_frequent == '':
                most_frequent = "R"

            ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
            guess = ideal_response[most_frequent]

        else:
            # Counter Abby strategy
            last_two = "".join(my_history[-2:])
            if len(last_two) == 2:
                play_order[0][last_two] += 1

            potential_plays = [
                my_history[-1] + "R",
                my_history[-1] + "P",
                my_history[-1] + "S",
            ]

            sub_order = {
                k: play_order[0][k]
                for k in potential_plays if k in play_order[0]
            }

            prediction = max(sub_order, key=sub_order.get)[-1:]

            ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
            guess = ideal_response[prediction]
    else:
        guess = "P"

    my_history.append(guess)
    return guess
