# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an
# unknown given number.
import random
def func(n):
    x = random.randint(0,100)
    print('random number', x)
    return n*x


n=int(input('enter a number'))
print(func(n))