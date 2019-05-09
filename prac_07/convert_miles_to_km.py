"""
CP1404 Practical
Kivy GUI program to convert miles to kilometers
Lukas Arnold
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

__author__ = 'Lukas Arnold'

MILES_TO_KILOMETRES = 1.60934


class ConvertDistanceUnitApp(App):
    """ ConvertDistanceUnitApp is a Kivy App for converting miles to kilometers """
    message = StringProperty()

    def build(self):
        """ Build the Kivy app from the kv file """
        Window.size = (300, 250)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_press(self):
        self.message = self.root.ids.user_input.text

    def handle_conversion_to_km(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
#        value = self.handle_invalid_input()
        result = value * MILES_TO_KILOMETRES
        self.root.ids.output_label.text = str(result)

    def handle_increment_up(self, value):
        result = value + 1
        self.root.ids.input_number.text = str(result)

    def handle_increment_down(self, value):
        result = value - 1
        self.root.ids.input_number.text = str(result)

    def handle_invalid_input(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0.0


ConvertDistanceUnitApp().run()
