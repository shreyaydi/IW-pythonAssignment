# Write a Python program to clone or copy a list.
def func(my_input):
    old_list = my_input.split(' ')
    new_list = list(old_list)
    return old_list, new_list


my_input = (input("Enter a list elements separated by a space "))
print(func(my_input))
