"""
Program to estimate an electricity bill for
a user defined period, usage and price.
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity Bill Estimator")
user_input = str(input("Choose your method of estimation:\n a) Estimate by choosing an estimated price per kWh\n b) Estimate by choosing either Tariff 11 or Tariff 31\n :"))

if user_input == "a":
    cents_per_kWh = float(input("Enter price per kWh: $"))
    daily_use_kWh = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))
    bill = cents_per_kWh * daily_use_kWh * billing_days
    print("Your estimated bill is: ${}".format(bill))

elif user_input == "b":

    tariff = str(input("Choose which tariff:\n c) Tariff_11\n d) Tariff_31\n :"))

    if tariff == "c":
        daily_use_kWh = float(input("Enter daily use in kWh: "))
        billing_days = int(input("Enter number of billing days: "))
        bill = TARIFF_11 * daily_use_kWh * billing_days
        print("Your estimated bill is: ${}".format(bill))

    elif tariff == "d":
        daily_use_kWh = float(input("Enter daily use in kWh: "))
        billing_days = int(input("Enter number of billing days: "))
        bill = TARIFF_31 * daily_use_kWh * billing_days
        print("Your estimated bill is: ${}".format(bill))

    else:
        print("Invalid input. Restart and enter either c or d")

else:
    print("Invalid input. Restart and enter either a or b")