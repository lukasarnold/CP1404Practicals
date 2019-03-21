"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        denominator = int(input("Enter a non-zero denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")



# Questions
#
# When will a ValueError occur?  When a non-integer is selected for the inputs
# When will a ZeroDivisionError occur? When a 0 is choosen for a demoninator
# Could you change the code to avoid the possibility of a ZeroDivisionError? Yes if you apply an error checking command
# that asks the user to reinput the value of the denominator