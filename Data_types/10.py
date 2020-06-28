# Write a Python program to remove the characters which have odd index
# values of a given string.
def func(my_input):
    for i in range(len(my_input)):
        if i % 2 != 0:
            my_input = my_input.replace(my_input[i], ' ')
    return my_input.replace(' ','')



my_input = input('Enter the input\n')
print(func(my_input))