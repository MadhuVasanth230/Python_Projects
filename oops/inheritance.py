class Animal:

    def __init__(self, name):
        self.name = name

    def animalSound(self, sound):
        print(f"Animal {self.name} Sound is : {sound}")

    def animalSleep(self, sound):
        print(f"Animal {self.name} Sleep Sound is : {sound}")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


dog = Dog("Choo")
dog.animalSleep("zZz")
dog.animalSound("Bow-Bow")
