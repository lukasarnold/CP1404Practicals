"""
CP1404/CP5632 Practical
Word occurrences in a dictionary
"""

# Ask for user input
string = input("Enter a string: ")

# Create empty dictionary
words_and_counts = {}

# Split string into words and store in a list of words
words = string.split(" ")

# Check and count how many times a word is in words
word_counter = 0
for i in range(len(words)):
    for j in range(len(words)):
        if words[i] == words[j]:
            word_counter += 1
    words_and_counts['{}'.format(words[i])] = word_counter
    word_counter = 0



# Find longest word
for words, counts in words_and_counts.items():
    longest_word = max(words)

# Print output
print("Text: {}".format(string))

for words, counts in words_and_counts.items():
    print("{:{}} = {}".format(words, len(longest_word), counts))