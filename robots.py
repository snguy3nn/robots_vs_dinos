from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = 100
        self.health = 100
        self.weapon = Weapon("Rocket Launcher", 100)


