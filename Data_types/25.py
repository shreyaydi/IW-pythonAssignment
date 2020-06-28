# Write a Python program to check whether all dictionaries in a list are empty or
# not.
def func(list):
    for dict in list:
        if dict:
            return False
    return True


print(func([{}, {}, {}]))
print(func([{1, 2}, {}, {}]))