from abc import ABC, abstractmethod


class AbstractAnimal(ABC):

    @abstractmethod
    def bark(self):
        pass


class Dog(AbstractAnimal):

    def bark(self):
        print('Bow Bow')


dog = Dog()
print(Dog())
print(dog.bark())