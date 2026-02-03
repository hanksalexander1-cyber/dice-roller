from dice import dice_roller
from made import playerclass
import time
import os
starter = dice_roller(3)

def clear_screan():
    if os.name == 'nt':        
                _ = os.system('cls')

def player_interactive(player_names_class, rounds, score_to_be_played):
    current_player = player_names_class[rounds] 
    if current_player.score < score_to_be_played:
        print(f"current player is {current_player.name}")
        print(f"selected points is {score_to_be_played}")
        print(f"selected players current points is {current_player.score}")
        time.sleep(.7)
        ended = "yes"
        while ended != "no":
            if current_player.score < score_to_be_played:
                points = current_player.determine_points()
                if current_player.score >= score_to_be_played:
                    break
                if points == False:
                    input("press anything to coninue to the next player's turn: ")
                    print("starting next round...")
                    time.sleep(.5)
                    break
                
                stop = input("select either y/yes to stop or n/no to continue your turn: ").strip().lower()
                if stop in ["y","yes"]:
                    print("your turn has ended")
                    ended = "no"
                elif stop in ["n", "no"]:
                    continue
    return current_player

def game():
    for i in range(3):
        print("starting the game... ")
        time.sleep(.6)
        clear_screan()
    rounds = 0
    num_of_players = int(input("Enter the total amount of players in this session: "))
    score_to_be_played = int(input("Enter the score you would like to play to: "))

    player_names_class = []

    for player in range(num_of_players):
        player_name = input("Enter the name of a new player -> ")
        player_name = playerclass(name = player_name, score= 0)
        player_names_class.append(player_name)


    while True:
        current_player = player_names_class[rounds]
        player_interactive(player_names_class, rounds, score_to_be_played)
        if current_player.score >= score_to_be_played:
            print(f"{current_player.name} has reached the set points to be played until")
            print("the remaining players will have one last turn to try and beat the player in score")
            break
        rounds += 1
        if rounds >= num_of_players:
            rounds = 0
            print("starting new round")
            time.sleep(1.5)
            clear_screan()
    finalist = player_names_class[rounds]
            
    for player in player_names_class:
        if player != finalist:
            input("press anything to start the next players turn:")
            print(f"current player is {player.name}")
            print(f"selected players current points is {player.score}")
            player.determine_points()
            time.sleep(1)
    
    
    print("Final scores:")
    for player in player_names_class:
        print(f"{player.name} has the score of: {player.score}")
    
    winner = player_names_class[0]

    for player in player_names_class:
        if player.score > winner.score:
            winner = player
            print(f"Winner is {winner.name} with {winner.score} points")
        elif player.score == winner.score:
            print(f"the game ended in a tie")
            return

        



    

        
    #print(f"you gained {points_given} points")
    #player_list = {}
    #player_list[f"{player_name}"] = points_given
            
    



        






game()

