# Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).
n = int(input('input a number'))
dict = {}
for i in range(n):
    dict[i] = i * i
print(dict)