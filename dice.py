
import random




class dice_roller:

    dice_art = {
        1: ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
        3: ("┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
        5: ("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"),
        6: ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")
    }


    def __init__(self, num_dice:int = 3):
        self.num_dice = num_dice
        self.values = []
        for num in range(self.num_dice) :
            self.values.append(0)
    
    def roll(self):
        for i in range(self.num_dice):
            self.values[i] = random.randint(1,6)
    
    def get_total(self):
        total = 0 
        for num in self.values:
            total += num
        print(f"the total values of the die are {total}")

    def print_die(self):
        #for die in range(self.num_dice):
        #    for line in self.dice_art.get(self.values[die]):
        #        print(line)
        for line in range(5):
            for die in self.values:
                print(self.dice_art.get(die)[line], end = "")
            print()


#starter = dice_roller(3)

#starter.roll()
#starter.get_total()
#starter.print_die()