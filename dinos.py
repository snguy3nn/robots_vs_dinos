class Dinosaur:
    def __init__(self, dino_type, attack_power):
        self.dino_type = dino_type
        self.energy = 100
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f'{self.dino_type} attacks {robot.name} for {self.attack_power} damage. New health is {robot.health}')