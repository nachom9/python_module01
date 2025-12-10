#!/usr/bin/env python3

class GardenManager:

    garden = []

    def __init__(self, owner: str) -> None:
        """Initialize a GardenManager for the given owner.

        Args:
            owner (str): Name of the garden owner.
        """
        self.owner = owner
        self.garden = {
                "plants": [],
                "stats": {
                    "plants_added": 0,
                    "growth_total": 0
                    }
                }
        GardenManager.garden.append(self)

    def add_plant(self, plant: "Plant") -> None:
        """Add a plant object to this garden and update stats.

        Args:
            plant (Plant): An instance of Plant or a subclass.
        """
        self.garden["plants"].append(plant)
        self.garden["stats"]["plants_added"] += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        """Increase height of every plant in this garden by 1cm and update
        stats.
        """
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.garden["plants"]:
            plant.height += 1
            self.garden["stats"]["growth_total"] += 1
            print(f"{plant.name} grew 1cm")

    def get_info(self) -> None:
        """Print a human-readable report of the plants contained in this
        garden.
        """
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.garden["plants"]:
            info = f"- {plant.name}: {plant.height}cm"
            cls_name = plant.__class__.__name__
            if cls_name == "FloweringPlant" or cls_name == "PrizeFlower":
                info += f", {plant.color} flowers"
                if plant.bloom:
                    info += " (blooming)"
                if cls_name == "PrizeFlower":
                    info += f", Prize points: {plant.prize_points}"
            print(info)

    class GardenStats:

        @staticmethod
        def calculate_points(garden: "GardenManager") -> int:
            """Calculate total prize points for a single garden.

            Args:
                garden (GardenManager): The garden to calculate points for.

            Returns:
                int: Sum of prize_points of PrizeFlower instances in the
                garden.
            """
            total_points = 0
            for plant in garden.garden["plants"]:
                if plant.__class__.__name__ == "PrizeFlower":
                    total_points += plant.prize_points
            return total_points

        @staticmethod
        def count_regular(garden: "GardenManager") -> int:
            """Count how many regular Plant instances are in the given
            garden.
            """
            count = 0
            for plant in garden.garden["plants"]:
                if plant.__class__.__name__ == "Plant":
                    count += 1
            return count

        @staticmethod
        def count_flowering(garden: "GardenManager") -> int:
            """Count how many FloweringPlant instances are in the given
            garden.
            """
            count = 0
            for plant in garden.garden["plants"]:
                if plant.__class__.__name__ == "FloweringPlant":
                    count += 1
            return count

        @staticmethod
        def count_prize(garden: "GardenManager") -> int:
            """Count how many PrizeFlower instances are in the given garden."""
            count = 0
            for plant in garden.garden["plants"]:
                if plant.__class__.__name__ == "PrizeFlower":
                    count += 1
            return count

    @classmethod
    def create_garden_network(cls) -> None:
        """Perform class-level analytics over all gardens and print a summary.

        This method validates heights across all gardens, computes garden
        scores and prints the total number of gardens managed.
        """
        height_check = True
        for gardens in cls.garden:
            for plant in gardens.garden["plants"]:
                if plant.height < 0:
                    height_check = False
        print(f"Height validation test: {height_check}")
        flag = 0
        info = "Garden scores - "
        for gardens in cls.garden:
            total_points = 0
            if flag != 0:
                info += ", "
            total_points = cls.GardenStats.calculate_points(gardens)
            info += f"{gardens.owner}: {total_points}"
            flag = 1
        print(info)
        total_gardens = 0
        for gardens in cls.garden:
            total_gardens += 1
        print(f"Total gardens managed: {total_gardens}")


class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        """Base plant with common attributes.

        Args:
            name (str): Plant name.
            height (int): Plant height in centimeters.
            age (int): Plant age in days.
        """
        self.name = name
        self.height = height
        self.age = age


class FloweringPlant(Plant):

    def __init__(self, name: str, height: int, age: int, color: str,
                 bloom: bool) -> None:
        """A plant that can produce flowers.

        Args:
            color (str): Flower color.
            bloom (bool): Whether the plant is currently blooming.
        """
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom


class PrizeFlower(FloweringPlant):

    def __init__(self, name: str, height: int, age: int, color: str,
                 bloom: bool, prize_points: int) -> None:
        """A flowering plant that awards prize points.

        Args:
            prize_points (int): Points awarded by this plant.
        """
        super().__init__(name, height, age, color, bloom)
        self.prize_points = prize_points


def main():
    """Demonstrates how to create gardens, add plants, grow plants, and
    prints all necessary information"""
    print("=== Garden Management System Demo ===\n")
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")
    spruce = Plant("Spruce", 80, 400)
    oak = Plant("Oak Tree", 100, 500)
    rose = FloweringPlant("Rose", 25, 20, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, 20, "yellow", True, 10)
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    bob.add_plant(spruce)
    print("")
    alice.grow_all()
    print("")
    alice.get_info()
    print("")
    print(f"Plants added: {alice.garden['stats']['plants_added']}"
          f", Total growth: {alice.garden['stats']['growth_total']}cm")
    print(f"Plant types: {GardenManager.GardenStats.count_regular(alice)} "
          f"regular, "
          f"{GardenManager.GardenStats.count_flowering(alice)} flowering, "
          f"{GardenManager.GardenStats.count_prize(alice)} prize flowers\n")
    GardenManager.create_garden_network()


if __name__ == "__main__":
    main()
