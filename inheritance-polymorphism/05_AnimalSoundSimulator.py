# Problem 5: Animal Sound Simulator
# Scenario: Animal sound simulation
# Task: Override make_sound() method

class Animal:

    def make_sound(self):
        print("Animal sound")


class Dog(Animal):

    def make_sound(self):
        print("Woof!")


class Cat(Animal):

    def make_sound(self):
        print("Meow!")


# Looping through objects
for animal in [Dog(), Cat()]:
    animal.make_sound()