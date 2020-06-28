# Write a Python program to replace the last element in a list with another list.
def func(my_input1, my_input2):
    list1 = (my_input1.split(' '))
    list2 = (my_input2.split(' '))
    numbers1 = []
    numbers2 = []
    final = []
    for input in list1:
        numbers1.append(int(input))
    for input in list1:
        numbers1.append(int(input))
    output = list1[:-1] + list2
    for input in output:
        final.append(int(input))

    return final

my_input1 = (input("Enter first list elements separated by a space "))
my_input2 = (input("Enter second list elements separated by a space"))
print(func(my_input1, my_input2))