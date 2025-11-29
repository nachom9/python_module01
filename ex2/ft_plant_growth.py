#!/usr/bin/env python

class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def garden_growth(self):
        i = 1
        while (i <= 7):
            print(f"=== Day {i} ===")
            print(f"{self.name}: {self.height}cm, {self.age} days old")
            grow(self)
            age(self)
            i += 1
        else:
            print(f"Growth this week: +{i - 2}cm")


rose = plant("Rose", 25, 30)


def grow(plant):
    plant.height += 1


def age(plant):
    plant.age += 1


rose.garden_growth()
