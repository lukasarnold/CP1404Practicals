"""
SilverServiceTaxi Class test code
Lukas Arnold
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """"""

    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.drive(18)
    print(taxi)
    print("Total taxi fare: ")
    print(taxi.get_fare())


main()
