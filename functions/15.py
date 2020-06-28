# Write a Python program to filter a list of integers using Lambda.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list ")
print(num)
print("\nEven numbers ")
even_num = list(filter(lambda x: x%2 == 0, num))
print(even_num)
print("\nOdd numbers ")
odd_num = list(filter(lambda x: x%2 != 0, num))
print(odd_num)