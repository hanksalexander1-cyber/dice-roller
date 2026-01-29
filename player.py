from dice import dice_roller
from farkle_game import rolled
from farkle_game import player_name
starter = dice_roller(3)

class playerclass:

    def __init__(self, name:str, score:int):
        self.name = name
        self.score = score
        

    def conditions(self):
        while True:
            values = rolled
            points_given = 0
            for value in values:
                if value == value:
                    points_given + 500
                    print("you rolled 3 of a kind and was given 500 points")
                    continue
                elif value == 1:
                    points_given + 100
                elif value == 5:
                    points_given + 50
                elif value != value:
                    print("you rolled a farkle and were given 0 points")
                    exit
            print(f"current player is {player_names[0]}")
            rolled = starter.roll()
            print(f"your dice are ------> {starter.print_die()}")
            self.score + points_given
            return points_given
