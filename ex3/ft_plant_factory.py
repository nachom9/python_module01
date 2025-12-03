class Plant:
    """Class representing a basic plant with height and age tracking."""

    plant_count = 0

    def __init__(self, name: str, st_height: int, st_age: int) -> None:
        """Initialize a Plant and increment the total plant count.

        Args:
            name (str): Name of the plant.
            st_height (int): Height of the plant in centimeters.
            st_age (int): Age of the plant in days.
        """
        self.name = name
        self.st_height = st_height
        self.st_age = st_age
        Plant.plant_count += 1
        print(f"Created: {self.name} ({self.st_height}cm, {self.st_age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunfower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    print(f"\nTotal plants created: {Plant.plant_count}")
