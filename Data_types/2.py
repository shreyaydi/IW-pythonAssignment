# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the
# string length is less than 2, return instead of the empty string.
def func(my_input):
    if len(my_input) < 2:
        return 'Empty String'
    else:
        output = my_input[0:2] + my_input[-2:]
        return output


my_input = input('Enter the input\n')
print(func(my_input))