"""
Sort Files Code 2
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

    # Delete repeating file extensions
    extensions = []
    for extension in all_extensions:
        if extension not in extensions:
            extensions.append(extension)

    # Ask user what directory to store all extension types under
    extension_to_sub_directory = {}
    for extension in extensions:
        sub_directory = input("What category would uou like to sort {} files into?".format(extension))
        extension_to_sub_directory[extension] = sub_directory
    print(extension_to_sub_directory)

    # Extract from dictionary the sub directory names
    sub_directory_extensions = []
    for key, value in extension_to_sub_directory:
        sub_directory_extensions.append(key)

    # Delete repeating sub directories
    new_subdirectories = []
    for extension in sub_directory_extensions:
        if extension not in new_subdirectories:
            new_subdirectories.append(extension)

    # Create Sub directories
    try:
        for key, value in extension_to_sub_directory:
            os.mkdir(key)
    except FileExistsError:
        pass

    # Move files to directories
    for i in range(len(files)):
        for j in range(len(extensions)):
            shutil.move(files[i], key[j])


main()
