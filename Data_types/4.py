#Write a Python program to get a single string from two given strings, separated
#by a space and swap the first two characters of each string.
def func(my_input1, my_input2):
    string1 = my_input2[:2] + my_input1[2:]
    string2 = my_input1[:2] + my_input2[2:]
    output = string1 + " " + string2
    return output


my_input1 = input('Enter the first string\n')
my_input2 = input('Enter the second string\n')
print(func(my_input1, my_input2))