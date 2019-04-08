"""CP1404/CP5632 Practical - Programming Language."""


class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, language=""):
        """Initialise the Programming Language Instance

        language: string, name of programming language"""
        self.language = language

    def __str__(self):
        """Return the representation of the programming language object"""
        return "{}".format(self.language)
