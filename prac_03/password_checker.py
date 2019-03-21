"""
Warm up question password check
"""

password = str(input("Enter a password for checking: "))
MIN_NO_CHARACTERS = 6

if len(password) >= MIN_NO_CHARACTERS:
    print("Your password meets the minimum length requirement!")
    print("*" * len(password))
else:
    print("Your password does not meet the minimum length requirement! Restart program.")


# def version_1():
#     """Get a password of valid size and print asterisks."""
#     password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
#     while len(password) < MINIMUM_LENGTH:
#         password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
#
#     print('*' * len(password))
#
#
# # version_1()
#
#
# def main():
#     """Get and print password using functions."""
#     password = get_password(MINIMUM_LENGTH)
#     print_asterisks(password)
#
#
# def get_password(minimum_length):
#     """Get password, ensuring it meets the minimum_length requirement."""
#     password = input("Enter password of at least {} characters: ".format(minimum_length))
#     while len(password) < minimum_length:
#         print("Password too short")
#         password = input("Enter password of at least {} characters: ".format(minimum_length))
#     return password
#
#
# def print_asterisks(sequence):
#     """Print as many asterisks as there are characters in the passed-in sequence."""
#     print('*' * len(sequence))
#
#
# main()