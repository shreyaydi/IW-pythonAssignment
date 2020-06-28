# Write a Python program to square and cube every number in a given list of integers using Lambda.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list ")
print(num)
print("\nSquare numbers :")
square_num = list(map(lambda x: x ** 2, num))
print(square_num)
print("\nCube numbers:")
cube_num = list(map(lambda x: x ** 3, num))
print(cube_num)
