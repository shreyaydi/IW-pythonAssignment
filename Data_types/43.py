# Write a Python program to remove an item from a tuple.
tuples = (1, 2, 3, 4, 5)
print (tuples)
tuples = tuples[:1] + tuples[2:]
print(tuples)
list = list(tuples)
list.remove(1)
tuples = tuple(list)
print(tuples)
