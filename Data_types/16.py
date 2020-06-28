# Write a Python program to sum all the items in a list.
def func(my_input):
    list = my_input.split(' ')
    sum_list = 0
    for i in list:
        sum_list += int(i)
    return sum_list


my_input = (input("Enter a list elements separated by a space "))
print(func(my_input))