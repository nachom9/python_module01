#!/usr/bin/env python

class plant:

    def __init__(self, name, st_height, st_age):
        self.__name = name
        self.__st_height = st_height
        self.__st_age = st_age
        print(f"Plant created: {self.__name}")

    def set_height(plant, height):
        if height >= 0:
            plant.__st_height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height "
                  f"{height}cm [REJECTED]")
            print("Security: Negative height rejected")
            print(f"\nCurrent plant: {plant.__name} "
                  f"({plant.__st_height}cm {plant.__st_age} days)")

    def set_age(plant, age):
        if age >= 0:
            plant.__st_age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print("\nInvalid operation attempted: "
                  f"age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            print(f"\nCurrent plant: {plant.__name} "
                  f"({plant.__st_height}cm {plant.__st_age} days)")

    def get_height(plant):
        return plant.__st_height

    def get_age(plant):
        return plant.__st_age


print("=== Garden Security System ===")
rose = plant("Rose", 10, 10)
plant.set_height(rose, 25)
plant.set_age(rose, 30)
plant.set_height(rose, -5)
