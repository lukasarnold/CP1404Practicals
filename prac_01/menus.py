"""
Talks back to the user based on the menu option they choose
"""

#TODO finish this program

name = str(input("What is your first name?"))
choice = str(input(" Choose your option:\n (H)ello\n (G)oodbye\n (Q)uit\n :"))
while choice != "Q":
   if choice == "H":
       print("Hello {}".format(name))
   elif choice == "G":
       print("Goodbye {}".format(name))
else:
       print("Invalid input")
