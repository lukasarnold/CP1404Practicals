"""
SilverServiceTaxi Class
Lukas Arnold
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """ """

    # set flagfall price
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """ """
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """ """
        return self.flagfall + super().get_fare()
