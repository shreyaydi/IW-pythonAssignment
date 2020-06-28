# Write a Python function to check whether a number is in a given range.
def func(n):
    if n in range(0,9):
        return ('In range')
    else:
        return('Not in range')


n = int(input('enter a number'))
print(func(n))
