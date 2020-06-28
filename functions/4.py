# Write a Python program to reverse a string.
def func(my_input):
    output = ''
    for i in my_input:
        output = i + output
    return output



my_input = input('Enter the input\n')
print(func(my_input))
