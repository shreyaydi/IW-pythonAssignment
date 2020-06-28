# Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).
def func(my_input):
    words = my_input.split(',')
    counts = dict()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return sorted(counts)


my_input = input('Enter the input\n')
print(func(my_input))