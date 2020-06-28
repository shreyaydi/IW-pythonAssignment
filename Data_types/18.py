# Write a Python program to get the largest number from a list.
def func(my_input):
    list = my_input.split(' ')
    max = list[0]
    for i in range(len(list)):
        if (list[i]) > max:
            max = list[i]
    return max


my_input = (input("Enter a list elements separated by a space "))
print(func(my_input))