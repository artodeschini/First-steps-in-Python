class LandAnimal:

    def __init__(self):
        super().__init__()
        self.walking_speed = 5

    def run(self):
        return self.walking_speed


class WaterAnimal:

    def __init__(self):
        super().__init__()
        self.swimming_spped = 15

    def swim(self):
        return self.swimming_spped


class Amphibian(LandAnimal,WaterAnimal): # sample with multiple inherit

    pass


animal = Amphibian()
print(animal)
print(animal.swim())
print(animal.run())