from dice import dice_roller
import time
starter = dice_roller(3)

class playerclass:

    def __init__(self, name:str, score:int):
        self.name = name
        self.score = score
        

    def determine_points(self):
        points_given = 0
        print("your die are as shown")
        values = starter.roll()
        starter.print_die()
        print(values)
        for value in values:
            if value == 1:
                points_given += 100
            if value == 5:
                points_given += 50
        if values[0] == values[1] and values[1] == values[2]:
            points_given = 0
            points_given += 500
            print("you rolled 3 of a kind and was given 500 points")
        elif values[0] not in [1,5] and values[1] not in [1,5] and values[2] not in [1,5]:
            points_given = 0
            print("you rolled a farkle and were given 0 points")
            time.sleep(.5)
            return False
                        
        self.score += points_given
        print(f"your score is currently {self.score} points")
