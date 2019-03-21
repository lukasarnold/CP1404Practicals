"""
Converts characters to ASCII integer values and vice versa
"""

character = str(input("Enter a character: "))
print("The ASCII code for {} is {}".format(character, ord(character)))

number = int(input("Enter a number between 33 and 127: "))
print("The character for {} is {}".format(number, chr(number)))
