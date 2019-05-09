"""
Kivy Practical Task 4 CP1404
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label

NAMES = ['Bob', 'Cat', 'Oren', 'Gary', 'Jim']


class SimpleDynamicWidgetsApp(App):

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Simple Dynamic Widgets"
        self.root = Builder.load_file('simple_dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from NAMES and add them to the GUI."""
        for name in NAMES:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)


SimpleDynamicWidgetsApp().run()
