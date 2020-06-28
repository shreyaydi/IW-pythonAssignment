# Write a Python program to add an item in a tuple.
tuples = (1, 2, 3, 4, 5)
print (tuples)
tuples = tuples + (6,)
print(tuples)
tuples = tuples[:5] + (7, 8, 9) + tuples[:5]
print (tuples)
list = list(tuples)
list.append(10)
tuples = tuple(list)
print(tuples)


