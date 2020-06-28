# Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
def func(my_input):
    pnot = my_input.find('not')
    ppoor = my_input.find('poor')
    if ppoor > pnot > 0:
        output = my_input.replace(my_input[pnot:(ppoor + 4)], 'good')
    elif ppoor > 0 and pnot == -1:
        output = my_input.replace(my_input[ppoor:ppoor + 4], 'good')
    else:
        output = my_input
    return output


my_input = input('Enter the input\n')
print(func(my_input))
