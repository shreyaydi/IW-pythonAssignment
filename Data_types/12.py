# Write a Python script that takes input from the user and displays that input
# back in upper and lower cases.
def func(my_input):
    return my_input.upper(), my_input.lower()


my_input = input('Enter the input\n')
print(func(my_input))