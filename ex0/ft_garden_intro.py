#!/usr/bin/env python3

def garden_intro() -> None:
    """
    Print a welcome message and display information about a single plant.

    This function defines basic plant data (name, height, age) and prints it
    in a formatted layout to the console.
    """
    name = "Rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


def main() -> None:
    """
    Entry point of the program.

    Calls the garden_intro() function and prints an ending message.
    """
    garden_intro()
    print("\n=== End of Program ===")


if __name__ == "__main__":
    main()
