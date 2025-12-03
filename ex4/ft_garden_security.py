class SecurePlant:
    """Class representing a plant with secure attribute access."""

    def __init__(self, name: str, st_height: int, st_age: int) -> None:
        """Initialize a SecurePlant with name, height, and age.

        Args:
            name (str): Name of the plant.
            st_height (int): Initial height in cm.
            st_age (int): Initial age in days.
        """
        self.__name = name
        self.__st_height = st_height
        self.__st_age = st_age
        print(f"Plant created: {self.__name}")

    def set_height(self, height: int) -> None:
        """Update the plant's height if valid, otherwise reject.

        Args:
            height (int): New height in cm.
        """
        if height >= 0:
            self.__st_height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height "
                  f"{height}cm [REJECTED]")
            print("Security: Negative height rejected")
            print(f"\nCurrent plant: {self.__name} "
                  f"({self.__st_height}cm, {self.__st_age} days)")

    def set_age(self, age: int) -> None:
        """Update the plant's age if valid, otherwise reject.

        Args:
            age (int): New age in days.
        """
        if age >= 0:
            self.__st_age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            print(f"\nCurrent plant: {self.__name} "
                  f"({self.__st_height}cm, {self.__st_age} days)")

    def get_height(self) -> int:
        """Return the plant's current height.

        Returns:
            int: Current height in cm.
        """
        return self.__st_height

    def get_age(self) -> int:
        """Return the plant's current age.

        Returns:
            int: Current age in days.
        """
        return self.__st_age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 10, 10)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
