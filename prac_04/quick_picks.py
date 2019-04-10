"""
QUICK PICKS LOTTERY TICKET GENERATOR
"""

import random

NUMBER_OF_NUMBERS_PER_QUICK_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

number_of_quick_picks = int(input("Enter how many quick picks:"))

while number_of_quick_picks < 0:
    print("Choose a valid number of quick picks!")
    number_of_quick_picks = int(input("Enter how many quick picks:"))

for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBER_OF_NUMBERS_PER_QUICK_PICK):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.append(number)
        while number in quick_pick:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.sort()
    # print(quick_pick)
    print(" ".join("{:2}".format(number) for number in quick_pick))
