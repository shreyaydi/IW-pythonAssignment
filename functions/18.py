# Write a Python program to check whether a given string is number or not using Lambda.

string = input('enter the string: ')

check = lambda x: True if x.isnumeric() else False

print(check(string))