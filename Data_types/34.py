# Write a Python script to merge two Python dictionaries.
def concat(dic1, dic2):
    dict = {}
    dict.update(dic1)
    dict.update(dic2)
    return(dict)


dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}

print(concat(dic1, dic2, dic3))
