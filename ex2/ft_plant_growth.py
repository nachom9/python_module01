class Plant:

    def __init__(self, name, height, time):
        self.name = name
        self.height = height
        self.time = time

    def age(self):
        self.time += 1

    def grow(self):
        self.height += 1

    def get_info(self):
        print(f"{self.name}, {self.height}cm, {self.time} days old")


if __name__ == "__main__":
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
