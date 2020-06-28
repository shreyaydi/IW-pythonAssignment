# Write a Python program to remove the nth index character from a nonempty string.
def func(my_input, n):
    output = my_input[:n] + my_input[n+1:]
    return output


my_input = input('Enter the string')
n = int(input('Enter the nth string to be removed'))

print(func(my_input, n))


