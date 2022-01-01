from stuff.Armor import *
from stuff.Weapon import *
from character.Barbarian import *
from character.Wizard import *
from Fight import *

sword = Weapon('sword', 8)
axe = Weapon('axe', 6)

breastplate = Armor('breastplate', 10)
gloves = Armor('gloves', 8)

barbarian = Barbarian(80, 'Sylent', axe, breastplate)
wizard = Wizard(65, 'Isindra', sword, gloves, 12, 10)

arena = Fight(barbarian, wizard)
arena.round()
