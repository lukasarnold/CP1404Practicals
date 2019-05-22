"""
Sort Files Code 1
Lukas Arnold
"""

import shutil
import os


def main():
    """ """

    os.chdir('FilesToSort')
    print("\nStarting directory is: {}".format(os.getcwd()))
    print("\nFiles in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Find all types of extensions
    all_extensions = []
    files = os.listdir('.')
    for file in files:
        split_files = file.split('.')
        all_extensions.append(split_files[1])
    all_extensions.sort()
    print(all_extensions)

    # Delete repeating file extensions
    extensions = []

    for extension in all_extensions:
        if extension not in extensions:
            extensions.append(extension)

    print(extensions)


main()
