# Write a Python function that takes a number as a parameter and check the number is prime or not.
def func(n):
    count = 0
    for i in range(1, n+1):
        if n%i == 0:
            count += 1
    if count < 3 :
        return 'Prime number'
    else:
        return 'Not a prime number'


n = int(input('Enter a number'))
print(func(n))