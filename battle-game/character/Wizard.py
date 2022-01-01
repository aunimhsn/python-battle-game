from stuff.Armor import *
from stuff.Weapon import *
from . import Character


class Wizard(Character.Character):
    def __init__(self, hp:int, name:str, weapon:Weapon, armor:Armor, spell:int, mana:int):
        self.hp = hp
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.spell = spell
        self.mana = mana

    def attack(self, character:Character):
        while True:
            print(f'Wizard {self.name} Turn:')
            choice = input('0 - Spell, 1 - Normal Attack: ')

            if choice == '0':
                self.mana -= 5
                character.hp -= self.spell
                print(f'The wizard {self.name} attacks {character.name} and do {self.spell} damage with his spell. {character.name} {character.hp} hp left.')
                break
            elif choice == '1':
                character.hp -= self.weapon.damage
                print(f'The wizard {self.name} attacks {character.name} and do {self.weapon.damage} damage with his weapon. {character.name} {character.hp} hp left.')
                break
            else:
                continue

    def receive_attack(self, weapon:Weapon):
        pass