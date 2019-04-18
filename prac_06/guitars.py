"""CP1404/CP5632 Practical - Client code to use the Guitar class."""
# Note that the import has a folder (module) in it.

from prac_06.guitar import Guitar


def main():
    """Program that uses Guitar class."""

    # Create empty list to store all guitars
    guitars = []

    # Print welcome message
    print("My Guitars!\n")

    # Ask for inputs and call class then store in list
    name = input("Name:")
    while name != "":
        year = int(input("Year:"))
        cost = float(input("Cost: $"))

        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print("{} ({}) : ${:.2f} added.\n".format(name, year, cost))

        name = input("Name:")

    # Add two guitars you already own
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # Print the guitars you own
    print("\nThese are my Guitars:")
    for guitar in range(len(guitars)):
        name = guitars[guitar].name
        year = guitars[guitar].year
        cost = guitars[guitar].cost

        # vintage_status = ""
        # if guitars[guitar].is_vintage():
        #     vintage_status = "(vintage)"

        vintage_status = "(vintage)" if guitars[guitar].is_vintage() else ""

        print("Guitar {}: {} ({}), worth ${:.2f} {}".format(guitar + 1, name, year, cost, vintage_status))


main()
