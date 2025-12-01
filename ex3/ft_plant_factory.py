class Plant:
    plant_count = 0

    def __init__(self, name, st_height, st_age):
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
