# Write a Python function to calculate the factorial of a number (a non-negative integer).
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)


n = int(input('enter the input'))
print(factorial(n))
