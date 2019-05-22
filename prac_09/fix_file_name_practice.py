filename = "SilentNight.TXT"

enumerated_filename = list(enumerate(filename))

new_filename = ""
for i in range(len(enumerated_filename)):
    new_filename = new_filename + filename[i]
    if str(enumerated_filename[i][1]) == ".":
        break
    else:
        if str(enumerated_filename[i][1]).islower and str(enumerated_filename[i + 1][1]).isupper():
            new_filename = new_filename + "_"
new_filename = new_filename + filename[i + 1:].lower()
print(new_filename)
