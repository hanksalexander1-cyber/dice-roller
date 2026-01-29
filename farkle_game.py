from dice import dice_roller
from player import playerclass
import time
import os
starter = dice_roller(3)



def game():
    num_of_players = int(input("Enter the total amount of players in this session: "))
    score_to_be_played = int(input("Enter the score you would like to play to: "))

    player_names = []

    for player in range(num_of_players):
        player_name = input("Enter the name of a new player -> ")
        player_names.append(player_name)
    playerstarter = playerclass(name = player_name)
    
    for i in range(3):
        print("starting the game... ")
        time.sleep(.6)
        if os.name == 'nt':        
            _ = os.system('cls')
    

        
    print(f"you gained {points_given} points")
    player_list = {}
    player_list[f"{player_name}"] = points_given
            
    return rolled

rolled = game()

        






game()