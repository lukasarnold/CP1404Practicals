"""
Program to calculate and display a user's total price
of items including a 10% discount when they spend
over $100.
"""
total = 0

number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total += price_of_item

if total > 100:
    total *= 0.9

print("The total price for {} items is ${:.2f}".format(number_of_items, total))
