"""CP1404/CP5632 Practical - Client code to use the ProgrammingLanguages class."""
# Note that the import has a folder (module) in it.

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Code to see how class ProgrammingLanguages works"""

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)


main()
