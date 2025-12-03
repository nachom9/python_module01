class Plant:
    """Represents a plant with basic height and age information."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Height of the plant in centimeters.
            age (int): Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def garden_data(self) -> None:
        """Print the plant's data in a readable format."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    rose.garden_data()
    sunflower.garden_data()
    cactus.garden_data()
