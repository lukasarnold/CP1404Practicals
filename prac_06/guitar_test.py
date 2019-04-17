"""CP1404/CP5632 Practical - Client code to use the Guitar class."""
# Note that the import has a folder (module) in it.

from prac_06.guitar import Guitar

CURRENT_YEAR = 2019


def main():
    """Code to see how class Guitar works"""

    # Add to guitars using Guitar class
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2012, 1000)

    # Test to see if get_age method works
    print("{} get_age() - Expected {}. Got {}".format(gibson.name, 97,
                                                      gibson.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(another_guitar.name, 7,
                                                      another_guitar.get_age()))

    # Test to see if is_vintage method works
    print("{} is_vintage() - Expected {}. Got {}".format(gibson.name,
                                                         True,
                                                         gibson.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another_guitar.name,
                                                         False,
                                                         another_guitar.is_vintage()))


main()
