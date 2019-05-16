
filename = "AwayInAManger.TXT"

enumerated_filename = list(enumerate(filename))

for i in range(len(enumerated_filename)):
    if str(enumerated_filename[i][1]).islower and str(enumerated_filename[i+1][1]).isupper():
        new_name = filename.replace(str(enumerated_filename[i+1][1]), " ")


print(new_name)

