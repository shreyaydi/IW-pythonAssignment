# Write a Python program to count the number of characters (character frequency) in a string.
def number_of_characters(my_input):
    counts = dict()
    for words in my_input:
        letters = words.split()
        for letter in letters:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
    return counts


my_input = input('Enter the input\n')
print(number_of_characters(my_input))
