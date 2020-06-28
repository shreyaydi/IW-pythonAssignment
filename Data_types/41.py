# Write a Python program to convert a tuple to a string.
def convertTuple(tup):
    str = ''.join(tup)
    return str


tuple = ('i','n','s','i','g','h','t','W','o','r','k','s','h','o','p')
str = convertTuple(tuple)
print(str)