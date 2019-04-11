"""CP1404/CP5632 Practical - Programming Language."""


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
        """Return the representation of the guitar object"""
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Calculates age based off the year it was made"""
        age = 2019 - self.year
        return age

    def is_vintage(self):
        """Determines if vintage based on age condition"""
        if age >= 50:
            is_vintage = True
        else:
            is_vintage = False
        return is_vintage
