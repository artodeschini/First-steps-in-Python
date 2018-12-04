from abc import ABC, abstractclassmethod


class AbstractAnimal(ABC):

    @abstractclassmethod
    def bark(self):
        pass


class Dog(AbstractAnimal):

    def bark(self):
        print('Bow Bow')


dog = Dog()
print(Dog())
print(dog.bark())