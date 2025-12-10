#!/usr/bin/env python3

class Plant:
    """Class representing a basic plant with height and age tracking."""

    plant_count = 0

    def __init__(self, name: str, st_height: int, st_age: int) -> None:
        """
        Initialize a Plant and increment the total plant count.

        Args:
            name (str): Name of the plant.
            st_height (int): Height of the plant in centimeters.
            st_age (int): Age of the plant in days.
        """
        self.name = name
        self.st_height = st_height
        self.st_age = st_age
        Plant.plant_count += 1

    def get_info(self) -> None:
        """
        Print information about the plant, including its name, height, and age.

        This method provides a readable summary of the plant's key attributes
        in the format: "Created: <name> (<height>cm, <age> days)".
        """
        print(f"Created: {self.name} ({self.st_height}cm, {self.st_age} days)")


def main() -> None:
    """
    Main function to create multiple Plant instances and display
    the total number of plants created.
    """
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    plants = [rose, oak, cactus, sunflower, fern]
    for plant in plants:
        plant.get_info()
    print(f"\nTotal plants created: {Plant.plant_count}")


if __name__ == "__main__":
    main()
