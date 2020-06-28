# Write a Python program to get the smallest number from a list.
def func(my_input):
    list = my_input.split(' ')
    min = list[0]
    for i in range(len(list)):
        if (list[i]) < min:
            min = list[i]
    return min


my_input = (input("Enter a list elements separated by a space "))
print(func(my_input))