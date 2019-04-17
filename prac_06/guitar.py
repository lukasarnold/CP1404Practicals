"""CP1404/CP5632 Practical - Programming Language."""

CURRENT_YEAR = 2019
AGE_FOR_VINTAGE = 50


class Guitar:
    """Represent a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise the Guitar Instance

        name: string, name of guitar (make and model)
        year: integer, year made
        cost: float, cost in dollars
        """

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the representation of the guitar object."""
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Calculates age based off the year it was made."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determines if vintage based on age."""
        return self.get_age() >= AGE_FOR_VINTAGE
