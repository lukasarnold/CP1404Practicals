"""
Cleanup files code
Lukas Arnold
"""

import shutil
import os


def main():
    """ """

    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics/Christmas')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory but pass if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        os.rename(filename, new_name)
        shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""

    # Open File Name
    filename = filename
    print(filename)

    # Constants
    SPECIAL_CHARACTER = "("
    SPECIAL_CHARACTERS = " ", "("

    # Fix lower case letters after space to upper case
    enumerated_filename1 = list(enumerate(filename))
    capital_fixed_filename = ""

    for i in range(len(enumerated_filename1)):
        if str(enumerated_filename1[i - 1][1]) == " " or str(enumerated_filename1[i - 1][1]) in SPECIAL_CHARACTERS and \
                str(enumerated_filename1[i][1]).islower():
            fixed_letter = enumerated_filename1[i][1].upper()
            capital_fixed_filename = capital_fixed_filename + fixed_letter
        else:
            capital_fixed_filename = capital_fixed_filename + filename[i]

    print(capital_fixed_filename)

    # Fix spaces to underscores and fix lower case txt
    enumerated_filename2 = list(enumerate(capital_fixed_filename))

    new_filename = ""
    for i in range(len(enumerated_filename2)):
        if str(enumerated_filename2[i][1]) != " ":
            new_filename = new_filename + capital_fixed_filename[i]
        if str(enumerated_filename2[i][1]) == ".":
            break
        else:
            if str(enumerated_filename2[i][1]).islower and str(enumerated_filename2[i + 1][1]).isupper() or str(
                    enumerated_filename1[i + 1][1]) \
                    in SPECIAL_CHARACTER:
                new_filename = new_filename + "_"

    new_filename = new_filename + filename[i + 1:].lower()
    print(new_filename)

    return new_filename


main()
