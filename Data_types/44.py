# Write a Python program to slice a tuple.
tuples = (1, 2, 3, 4, 5)
print(tuples)
tuples = tuples[:3] + (7, 8, 9) + tuples[:5]
print (tuples)