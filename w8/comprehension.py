#!/usr/bin/env python3

my_list = [1, 2, 3, 4, 5]

# list comprehension
# [ (computation(var)) for (var) in (iterable) ]
squared_c = [ num**2 for num in my_list if num % 2 == 0 ]

# dict comprehensions: TODO

print(squared_c)
# squared_list = []
# for num in my_list:
#     squared_list.append(num**2)

# print(squared_list)