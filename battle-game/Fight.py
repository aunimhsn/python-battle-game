from character.Character import *


class Fight:
    def __init__(self, fighter_one:Character, fighter_two:Character):
        self.fighter_one = fighter_one
        self.fighter_two = fighter_two

    def round(self):
        # Flag to know which turn is
        turn = True
        while (self.fighter_one.hp > 0) and (self.fighter_two.hp > 0):
            if turn:
                self.fighter_one.attack(self.fighter_two)
                turn = False
            else:
                self.fighter_two.attack(self.fighter_one)
                turn = True

        # Game over message...
        if (self.fighter_one.hp <= 0):
            print(f'{self.fighter_one.name} lost.')

        if (self.fighter_two.hp <= 0):
            print(f'{self.fighter_two.name} lost.')

    def balance_sheet():
        pass


