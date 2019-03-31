"""
CP1404/CP5632 Practical
Basic list operations code
"""

# 1. Basic list operations

# numbers = []
#
# for i in range(5):
#     numbers.append(int(input("Number: ")))
#
# print("The first number is: {}".format(numbers[0]))
# print("The last number is: {}".format(numbers[-1]))
# print("The smallest number is: {}".format(min(numbers)))
# print("The largest number is: {}".format(max(numbers)))
# print("The average of the numbers is: {}".format(sum(numbers) / 5))

# 2. Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter Username: ")

if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")
