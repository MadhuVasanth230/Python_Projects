class Animal:
    def __init__(self):
        self.__name = "Animal"

    # Method-1
    def getName(self):
        return self.__name

    def setName(self, value):
        self.__name = value

    # Method-2
    def Name(self, val=None):
        if val == None:
            return self.__name
        else:
            self.__name = val


# object
animal = Animal()

# method 1
print(animal.getName())
animal.setName("DOG")
print(animal.getName())


# method 2
print(animal.Name())
animal.Name("Rabbit")
print(animal.Name())
