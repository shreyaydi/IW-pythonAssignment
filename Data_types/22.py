# Write a Python program to remove duplicates from a list.
def func(my_input):
    list = my_input.split(' ')
    dup_items = set()
    uniq_items = []
    for x in list:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)
    return uniq_items


my_input = (input("Enter a list elements separated by a space "))
print(func(my_input))
