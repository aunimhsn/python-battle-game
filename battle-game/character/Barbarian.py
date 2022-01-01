from stuff.Armor import *
from stuff.Weapon import *
from . import Character


class Barbarian(Character.Character):
    def __init__(self, hp:int, name:str, weapon:Weapon, armor:Armor):
        self.hp = hp
        self.name = name
        self.weapon = weapon
        self.armor = armor

    def attack(self, character:Character):
        character.hp -= self.weapon.damage * 2
        print(f'The barbarian {self.name} attacks {character.name} and do {self.weapon.damage} damage with his weapon. {character.name} {character.hp} hp left.')
    
    def receive_attack(self, weapon:Weapon):
        pass