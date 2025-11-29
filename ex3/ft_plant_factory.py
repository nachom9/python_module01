#!/usr/bin/env python

class plant:
    plant_count = 0

    def __init__(self, name, st_height, st_age):
        self.name = name
        self.st_height = st_height
        self.st_age = st_age
        plant.plant_count += 1
        print(f"Created: {self.name} ({self.st_height}cm, {self.st_age} days)")


print("=== Plant Factory Output ===")
rose = plant("Rose", 25, 30)
oak = plant("Oak", 200, 365)
cactus = plant("Cactus", 5, 90)
sunfower = plant("Sunflower", 80, 45)
fern = plant("Fern", 15, 120)
print(f"\nTotal plants created: {plant.plant_count}")
