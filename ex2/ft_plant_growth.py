#!/usr/bin/env python3

class Plant:
    """Represents a simple plant with height and age tracking."""

    def __init__(self, name: str, height: int, time: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Initial height of the plant in centimeters.
            time (int): Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.time = time

    def age(self) -> None:
        """Increase the age of the plant by one day."""
        self.time += 1

    def grow(self) -> None:
        """Increase the height of the plant by one centimeter."""
        self.height += 1

    def get_info(self) -> None:
        """Print information about the plant's name, height, and age."""
        print(f"{self.name}, {self.height}cm, {self.time} days old")


def main() -> None:
    """
    Main function to simulate a plant's growth over a week.

    Creates a Plant instance, prints its initial info, ages and grows
    it for 1 week, and prints the final information.
    """
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    days = 0
    while days < 6:
        rose.age()
        rose.grow()
        days += 1
    print("=== Day 7 ===")
    rose.get_info()
    print("Growth this week: +6cm")


if __name__ == "__main__":
    main()
