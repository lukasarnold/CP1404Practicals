"""
CP1404/CP5632 Practical
Word occurrences in a dictionary

Use sample input: this is a collection of words of nice words this is a fun thing is it
"""

# Ask for user input
string = input("Enter a string: ")

# Create empty dictionary
words_and_counts = {}

# Split string into words and store in a list of words
words = string.split(" ")

# Sort the dictionary by alphabetic order of words
words.sort()

# Find longest word and length
length_longest_word = max(len(word) for word in words)

# Check and count how many times a word is in words
for i in range(len(words)):
    word_counter = 0
    for j in range(len(words)):
        if words[i] == words[j]:
            word_counter += 1
    words_and_counts['{}'.format(words[i])] = word_counter


# Print output
print("Text: {}".format(string))
for words, counts in words_and_counts.items():
    print("{:{}} : {}".format(words, length_longest_word, counts))
