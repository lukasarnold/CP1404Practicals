"""
UnreliableCar test Code
Lukas Arnold
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Tests of some unreliable cars."""

    good_car = UnreliableCar("Good Car", 100, 80)
    bad_car = UnreliableCar("Bad Car", 100, 6)

    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))
        print(" ")

    print(good_car)
    print(bad_car)


main()
