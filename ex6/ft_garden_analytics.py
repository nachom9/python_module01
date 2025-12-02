class GardenManager:

    garden = []

    def __init__(self, owner):
        self.owner = owner
        self.garden = {
                "plants": [],
                "stats": {
                    "plants_added": 0,
                    "growth_total": 0
                    }
                }
        GardenManager.garden.append(self)

    def add_plant(self, plant):
        self.garden["plants"].append(plant)
        self.garden["stats"]["plants_added"] += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.garden["plants"]:
            plant.height += 1
            self.garden["stats"]["growth_total"] += 1
            print(f"{plant.name} grew 1cm")

    def get_info(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.garden["plants"]:
            info = f"- {plant.name}: {plant.height}cm"
            cls_name = plant.__class__.__name__
            if cls_name == "FloweringPlant" or cls_name == "PrizeFlower":
                info += f", {plant.color} flowers"
                if plant.bloom == True:
                    info += " (blooming)"
                if cls_name == "PrizeFlower":
                    info += f", Prize points: {plant.prize_points}"
            print(info)

    class GardenStats:
        
        @staticmethod
        def calculate_gardens():
            return len(GardenManager.garden)

class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class FloweringPlant(Plant):

    def __init__(self, name, height, age, color, bloom):
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom


class PrizeFlower(FloweringPlant):

    def __init__(self, name, height, age, color, bloom, prize_points):
        super().__init__(name, height, age, color, bloom)
        self.prize_points = prize_points


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")
    oak = Plant("Oak Tree", 100, 500)
    rose = FloweringPlant("Rose", 25, 20, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, 20, "yellow", True, 10)
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    print("")
    alice.grow_all()
    print("")
    alice.get_info()
    print("")
    print(f"Total gardens managed: {GardenManager.GardenStats.calculate_gardens()}")
