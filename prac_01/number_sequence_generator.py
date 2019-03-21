"""
Returns a number sequence based on an arithmetic choice between a lower and upper number limit
"""


X = int(input("Choose a number for the lower limit: "))
Y = int(input("Choose a number for the upper limit: "))

user_input = str(input("Choose your sequence type:\n a) Show all even numbers from X to Y\n b) Show the odd numbers from X to Y\n c) Show the squares from X to Y\n d) Exit the program\n :"))

if choice == "a":
    for i in range(X, Y):
        print(i, end=' ')

elif choice == "b":

elif choice == "c":

elif choice == "d":

else:
    print("Invalid input. Restart and enter either a, b, c or d")


#TODO finish this program
