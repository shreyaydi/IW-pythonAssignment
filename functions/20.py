# Write a Python program to find intersection of two given arrays using Lambda.
array_1 = [1, 2, 3, 4, 5, 6]
array_2 = [7, 9, 8, 5, 6]
intersect = list(filter(lambda x: x in array_1, array_2))

print(intersect)