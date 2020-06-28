# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def func(my_input):
    dict = {"UPPER_CASE":0, "LOWER_CASE":0}
    for c in my_input:
        if c.isupper():
           dict["UPPER_CASE"]+=1
        elif c.islower():
           dict["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", my_input)
    print ("No. of Upper case characters : ", dict["UPPER_CASE"])
    print ("No. of Lower case Characters : ", dict["LOWER_CASE"])


my_input = input('Enter the input\n')
(func(my_input))