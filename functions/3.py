# Write a Python function to multiply all the numbers in a list.
ef func(my_input):
    list = my_input.split(' ')
    prod_list = 1
    for i in list:
        prod_list *= int(i)
    return prod_list


my_input = (input("Enter a list elements separated by a space "))
print(func(my_input))