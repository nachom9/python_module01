#!/usr/bin/env python3

class Plant:
    """Base class representing a generic plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with name, height and age."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Represents a flower derived from Plant, with a color attribute."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a Flower with base Plant attributes plus color."""
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> None:
        """Print information about the flower."""
        print(f"{self.name} ({self.__class__.__name__}): "
              f"{self.height}cm, {self.age} days, {self.color} color")

    def bloom(self) -> None:
        """Simulate the flower blooming."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Represents a tree derived from Plant, with trunk diameter."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialize a Tree with base Plant attributes plus trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> None:
        """Print information about the tree."""
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        """Calculate and print approximate shade based on trunk diameter."""
        print(f"{self.name} provides {int(self.trunk_diameter * 1.56)} "
              f"square meters of shade")


class Vegetable(Plant):
    """Represents a vegetable, with harvest season and nutritional value."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """Initialize a Vegetable with Plant attributes,
        harvest season and nutritional value."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        """Print information about the vegetable."""
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


def main():
    """Example usage of the Plant, Flower, Tree and Vegetable classes."""
    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("Sunflower", 20, 25, "yellow")
    oak = Tree("Oak", 500, 1825, 50)
    spruce = Tree("Spruce", 450, 1800, 45)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    banana = Vegetable("Banana", 15, 40, "summer", "potasium")
    print("=== Garden Plant Types ===\n")
    rose.get_info()
    rose.bloom()
    print("")
    oak.get_info()
    oak.produce_shade()
    print("")
    tomato.get_info()
    print("")
    sunflower.get_info()
    sunflower.bloom()
    print("")
    spruce.get_info()
    spruce.get_info()
    print("")
    banana.get_info()


if __name__ == "__main__":
    main()
