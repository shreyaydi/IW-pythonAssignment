# Write a Python program to insert a given string at the beginning of all items in
# a list.
def func(my_input):
    list = (my_input.split(' '))
    numbers = []
    for input in list:
        numbers.append(int(input))
    for i in range(len(numbers)):
        numbers[i] = 'emp' + str(numbers[i])
    return numbers


my_input = (input("Enter a list elements separated by a space "))
print(func(my_input))
