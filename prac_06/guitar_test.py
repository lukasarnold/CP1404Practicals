"""CP1404/CP5632 Practical - Client code to use the Guitar class."""
# Note that the import has a folder (module) in it.

from prac_06.guitar import Guitar


def main():
    """Code to see how class Guitar works"""

    gibson = Guitar("Gibson L-5 CES,1922,16035.40")

    print(gibson)

main()
