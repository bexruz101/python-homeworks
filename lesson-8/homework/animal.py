# Define the Animal class as the parent class
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} says {self.sound}")


# Child classes inheriting from Animal
class Cow(Animal):
    def __init__(self):
        super().__init__("Cow", "Moo")


class Pig(Animal):
    def __init__(self):
        super().__init__("Pig", "Oink")


class Duck(Animal):
    def __init__(self):
        super().__init__("Duck", "Quack")


# Testing the farm model
if __name__ == "__main__":
    cow = Cow()
    pig = Pig()
    duck = Duck()

    cow.make_sound()
    pig.make_sound()
    duck.make_sound()
