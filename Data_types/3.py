# Write a Python program to get a string from a given string where all occurrences of its first char have been
# changed to '$', except the first char itself.
def func(my_input):
    temp = my_input[0]
    for i in range(len(my_input)):
        if my_input[i] == temp:
            my_input = my_input.replace(temp, '$')
        output = temp + my_input[1:]
    return output



my_input = input('Enter the input\n')
print(func(my_input))