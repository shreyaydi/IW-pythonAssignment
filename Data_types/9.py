# Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.
def func(my_input):
    return my_input[-1:] + my_input[1:-1] +my_input[0:1]


my_input = input('Enter the input\n')
print(func(my_input))