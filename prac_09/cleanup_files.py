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


# def get_fixed_filename(filename):
#     """Return a 'fixed' version of filename."""
#     for word in words
#     new_name = " "
#     new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
#     return new_name


main()
