class Animal:

    def __init__(self, name, noise):
        self.name = name
        self.noise = noise

    def __repr__(self):
        return repr((self.name, self.noise))

    def make_noise(self):
        print(f'The sound of {self.name} is {self.noise}')


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self,'Dog', 'Au au')


class Cat(Animal):

    def __init__(self):
        Animal.__init__(self,'Cat', 'Meaw')


cat = Cat()
dog = Dog()

pets = [cat, dog]

print(pets)

for p in pets:
    print(p)
    p.make_noise()
