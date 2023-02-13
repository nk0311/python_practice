mystring = 'hello'

# my_list = []

# for letter in mystring:
#     my_list.append(letter)


# print(my_list)

mylist = [letter for letter in mystring]
print(mylist)

celsius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)
