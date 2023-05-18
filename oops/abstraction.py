from abc import ABC, abstractclassmethod

# Making class as Abstract class


class Animal(ABC):
    @abstractclassmethod
    def eat(self):
        pass


class Rabbit(Animal):
    # Implementing Abstract Method
    def eat(self):
        print("Eating")


rab = Rabbit()
rab.eat()
