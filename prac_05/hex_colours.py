"""
CP1404/CP5632 Practical
Hex colours in a dictionary
"""

HEX_COLOURS = {"AliceBlue": "#f0f8ff", "blue1": "0000ff", "brown": "#a52a2a", "coral": "#ff7f50",
               "gold1": "#ffd700", "gray": "#bebebe", "HotPink": "ff69b4", "light": "eedd82",
               "medium": "#66cdaa", "pale": "#db7093"}

colour_name_input = input("Colour name:")

while colour_name_input != "":
    print("Colour code is: {}".format(HEX_COLOURS[colour_name_input]))
    colour_name_input = input("Colour name:")
