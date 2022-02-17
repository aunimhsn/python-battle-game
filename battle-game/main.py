from gears.Armor import *
from gears.Weapon import *
from spells.Spell import *
from characters.Barbarian import *
from characters.Wizard import *
from Fight import *


sword = Weapon('sword', 8)
axe = Weapon('axe', 6)

breastplate = Armor('breastplate', 10)
gloves = Armor('gloves', 8)

fireball = Spell('fireball', 10, 6)
bolt = Spell('fireball', 13, 9)

barbarian = Barbarian(80, 'Sylent', axe, breastplate)
wizard = Wizard(65, 'Isindra', sword, gloves, 80, fireball)

arena = Fight(barbarian, wizard)
arena.round()
