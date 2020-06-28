# Write a Python function that takes a list of words and returns the length of the
# longest one.
def func(my_input):
    list = my_input.split(',')
    max = len(list[0])
    max_word = list[0]
    for i in range(len(list)):
        if len(list[i]) > max:
            max = len(list[i])
            max_word = list[i]
    return max_word


my_input = input("Enter a list elements separated by a comma ")
print(func(my_input))

