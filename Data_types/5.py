# Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.
def func(my_input):
    if len(my_input) < 3:
        return my_input
    else:
        if my_input[-3:] == 'ing':
            return my_input + 'ly'
        else:
            return my_input + 'ing'


my_input = input('Enter the input\n')
print(func(my_input))
