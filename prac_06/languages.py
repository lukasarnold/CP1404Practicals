"""CP1404/CP5632 Practical - Client code to use the ProgrammingLanguages class."""
# Note that the import has a folder (module) in it.

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Code to see how class ProgrammingLanguages works"""

    java = ProgrammingLanguage("Java", "Static", True, 1995)
    c_plus_plus = ProgrammingLanguage("c_plus_plus", "Static", False, 1983)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)

    print(java)
    print(c_plus_plus)
    print(ruby)
    print(python)
    print(visual_basic)


main()
