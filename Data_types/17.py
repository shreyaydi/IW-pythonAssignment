# Write a Python program to multiplies all the items in a list.
def func(my_input):
    list = my_input.split(' ')
    prod_list = 1
    for i in list:
        prod_list *= int(i)
    return prod_list


my_input = (input("Enter a list elements separated by a space "))
print(func(my_input))