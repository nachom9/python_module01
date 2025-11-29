#!/usr/bin/env python

print("=== Garden Plant Registry ===")


class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def garden_data(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


rose = plant("Rose", "25", "30")
sunflower = plant("Sunflower", "80", "45")
cactus = plant("Cactus", "15", "120")
rose.garden_data()
sunflower.garden_data()
cactus.garden_data()
