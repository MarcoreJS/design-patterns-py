class Dog:

    """ A Simple dog class"""

    def __init__(self, name):
        self.__name = name

    def speak(self):
        return "Woof!"


class Cat:
    """ A Simple dog class"""

    def __init__(self, name):
        self.__name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):

    """The factory method"""

    pets = dict(dog=Dog("Jhin"), cat=Cat("Curie"))

    return pets[pet]


d = get_pet("dog")
c = get_pet("cat")

print d.speak()
print c.speak()
