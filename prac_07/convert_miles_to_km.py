"""
CP1404 Practical
Kivy GUI program to convert miles to kilometers
Lukas Arnold
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lukas Arnold'


class ConvertDistanceUnitApp(App):
    """ ConvertDistanceUnitApp is a Kivy App for converting miles to kilometers """
    def build(self):
        """ Build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_conversion_to_km(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = value * 1.609344
        self.root.ids.output_label.text = str(result)


ConvertDistanceUnitApp().run()