# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.
def func(my_input):
    list = my_input.split(' ')
    count = 0
    for word in list:
        if len(word) > 2 and word[0] == word[-1]:
                    count +=1
    return count


my_input = (input("Enter a list elements separated by a space "))
print(func(my_input))
