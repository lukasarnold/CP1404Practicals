"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""

    # Task 1
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    print(repeat_string("Python", 1))

    # Task 2
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"
    print(repeat_string("hi", 2))

    # Task 3
    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # Task 4
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    # Task 5
    test_car = Car()
    assert test_car.fuel == 0


run_tests()

# Task 6
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()


# Task 7
# (don't change the tests, change the function!)

# Task 8
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:

def phrase_to_sentence(phrase):
    """
    Change phrase to sentance by making the sentance start with a capital and end with a full stop.

    >>> phrase_to_sentence('hello')
    'Hello.'
    >>> phrase_to_sentence('It is an ex parrot.')
    It is an ex parrot.
    >>> phrase_to_sentence('my name is lukas')
    'My name is lukas.'
    """

    # 'hello' ->
    # 'It is an ex parrot.' -> 'It is an ex parrot.'
    # and one more you decide (one that is valid!)
    # test this and watch the tests fail

    # then write the body of the function so that the tests pass
    sentence = phrase.capitalize()
    if sentence[-1] != ".":
        sentence += '.'

    return sentence
