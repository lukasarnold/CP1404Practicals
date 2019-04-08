"""
CP1404/CP5632 Practical
Practice and Extension Work
Converting parallel lists to a dictionary

Sample list input:
> Date: (8, 4, 2019)
> Names: ["Jack", "Jill", "Harry", "John", "Garry"]
> DOB: [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982), (1, 2, 1979), (20, 11, 1992)]
"""

# Get inputs
#current_year = input("What is the date today (In the format '(dd, mm, yyyy)'):")
#names = input("Enter list of names:")
#dates_of_birth = input("Enter list of dob in same format as date, for each person:")

current_year = (8, 4, 2019)
names = ["Jack", "Jill", "Harry", "John", "Garry"]
dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982), (1, 2, 1979), (20, 11, 1992)]

# Create dictionary
names_and_dob = {}

# Store names and dob in dictionary
for name in range(len(names)):
    names_and_dob['{}'.format(names[name])] = dates_of_birth[name]

# Calculate age of each person and print output with name

for names, dob in names_and_dob.items():
    age = current_year - dob
    print("{} is {} years old".format(names, age))
