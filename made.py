from dice import dice_roller
starter = dice_roller(3)

class playerclass:

    def __init__(self, name:str, score:int):
        self.name = name
        self.score = score
        

    def determine_points(self):
        print("your die are as shown")
        values = starter.roll()
        for value in values:
            points_given = 0
            if values[0] == values[1] and values[1] == values[2]:
                points_given += 500
                print("you rolled 3 of a kind and was given 500 points")
                continue
            elif value == 1:
                points_given += 100
            elif value == 5:
                points_given += 50
            else:
                print("you rolled a farkle and were given 0 points")
                        
        self.score += points_given
        return points_given
