from stuff.Armor import *
from stuff.Weapon import *
from . import Character


class Character:
    def __init__(self, hp:int, name:str, weapon:Weapon, armor:Armor):
        self.hp = hp
        self.name = name
        self.weapon = weapon
        self.armor = armor

    def attack(self, character:Character):
        character.hp -= self.weapon.damage

    def receive_attack(self, weapon:Weapon):
        self.hp -= weapon.damage