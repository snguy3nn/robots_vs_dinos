from robots import Robot


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot1 = Robot("Bumblebee")
        robot2 = Robot("Optimus Prime")
        robot3 = Robot("Grimlock")
        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)