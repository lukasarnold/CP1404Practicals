"""CP1404/CP5632 Practical - Programming Language."""


class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, language="", typing="", reflection="", year=0):
        """Initialise the Programming Language Instance

        language: string, name of programming language
        typing: string, either static or dynamic
        reflection: boolean, reflection
        year: integer, year of appearance
        """

        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """..."""
        """Return the representation of the programming language object"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.language, self.typing,
                                                                           self.reflection, self.year)

    def is_dynamic(self):
        """..."""
        if self.typing == "Dynamic":
            is_dynamic = True
        elif self.typing == "Static":
            is_dynamic = False
        return is_dynamic
