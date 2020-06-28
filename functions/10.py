# Write a Python program to print the even numbers from a given list.
def func(my_input):
    words = my_input.split(' ')
    list = []
    evenList = []
    for word in words:
        list.append(int(word))
    print (list)
    for i in list:
        if i%2 == 0:
            evenList.append(i)
    return evenList


my_input = (input("Enter a list elements separated by a space "))
print(func(my_input))