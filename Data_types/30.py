# Write a Python script to check whether a given key already exists in a
# dictionary.
def func(dic, key):
    if key in dic:
        return "exists"
    else:
        return "does not exists"


dic = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
print(func(dic, 7))
print(func(dic, 2))