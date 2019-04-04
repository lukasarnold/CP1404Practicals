"""
CP1404/CP5632 Practical
Word occurrences in a dictionary
"""

# Ask for user input
string = input("Enter a string: ")

# Create empty dictionary
words_and_counts = {}

# Split string into words and store words as keys in dictionary
words = string.split(" ")

# Check and count how many times a word is in words
word_counter = 1
for word in words:
    if words[word] == words[word + 1]:
        word_counter += 1

# Find longest word
for words, counts in words_and_counts.items():
    longest_word = max(words)

# Print output
print("Text: {}".format(string))

for words, counts in words_and_counts.items():
    print("{:{}} = {}".format(x, y, z))