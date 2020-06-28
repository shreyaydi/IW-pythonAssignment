# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def func(my_input):
    list = my_input.split(' ')
    uniq_items = []
    for x in list:
        if x not in uniq_items:
            uniq_items.append(x)
    return uniq_items


my_input = (input("Enter a list elements separated by a space "))
print(func(my_input))