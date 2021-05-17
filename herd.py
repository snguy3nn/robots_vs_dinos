from dinos import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino1 = Dinosaur('T-Rex', 100)
        dino2 = Dinosaur('Raptor', 100)
        dino3 = Dinosaur('Triceratops', 100)
        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)
