from dice import dice_roller
from made import playerclass
import time
import os
starter = dice_roller(3)



def game():
    rounds = 0
    num_of_players = 1 #int(input("Enter the total amount of players in this session: "))
    score_to_be_played = 3 #int(input("Enter the score you would like to play to: "))

    player_names_class = []

    for player in range(num_of_players):
        player_name = input("Enter the name of a new player -> ")
        player_name = playerclass(name = player_name, score= 0)
        player_names_class.append(player_name)
    
    current_player = player_names_class[rounds]
    
    for i in range(3):
        print("starting the game... ")
        time.sleep(.6)
        if os.name == 'nt':        
            _ = os.system('cls')
    
    print(f"current player is {current_player.name}")
    time.sleep(.7)

    current_player.determine_points()
    

        
    #print(f"you gained {points_given} points")
    #player_list = {}
    #player_list[f"{player_name}"] = points_given
    print(player_names_class)
            
    



        






game()