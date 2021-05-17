from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = 100
        self.health = 100
        self.weapon = Weapon("Rocket Launcher", 100)

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(
            f'{self.name} attacks {dinosaur.dino_type} with a {self.weapon.weapon_type} for {self.weapon.attack_power} damge. New health is {dinosaur.health}')
