# Write a Python program to multiply all the items in a dictionary.
def prod(val):
    x = 1
    for key, value in val.items():
        x *= val[key]
    return x

dic1 = {1:10, 2:20}
print(prod(dic1))