# Write a Python program to count the occurrences of each word in a given
# sentence.
def func(my_input):
    words = my_input.split()
    counts = dict()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


my_input = input('Enter the input\n')
print(func(my_input))