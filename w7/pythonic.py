#!/usr/bin/env python3


# Looping over a collection 

# colors = ['red', 'green', 'blue', 'yellow']
# range(5) == [0, 1, 2, 3, 4]

# for i in range(len(colors)):
#     print(colors[i])

# for color in colors:
#     print(color)


# ####################


# Looping backwards

colors = ['red', 'green', 'blue', 'yellow']

# for i in range(len(colors)-1, -1, -1):
#     # print(i)
#     print(colors[i])

# for color in reversed(colors):
#     print(color)


#######################33

# colors = ['red', 'green', 'blue', 'yellow']

# for index, value in enumerate(colors):
#     print(f"{index} --> {value}")

# for i in range(len(colors)):
#     print(f"{i} --> {colors[i]}")

# names = ['raymond', 'rachel', 'matthew']
# colors = ['red', 'green', 'blue', 'yellow']

# n = min(len(names), len(colors))
# for i in range(n):
#     print (names[i], '--->', colors[i])

# for item1, item2 in zip(names, colors):
#     print(item1, item2, sep=", ", end="")


# colors = ['red', 'green', 'blue', 'yellow']

# Forward sorted order
# for color in sorted(colors):
#     print(color)

# Backwards sorted order
# for color in sorted(colors, reverse=True):
#     print(colors)



# Multiple exit points in a loop

def find(seq, target):
    for (i, value) in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

    # found = False
    # for i, value in enumerate(seq):
    #     if value == target:
    #         found = True
    #         break
    # if not found:
    #     return -1
    # return i

# list1 = [1, 3, 5]
# target = 6
# print(find(list1, target))



###### DICTIONARIES ##############################

# d = {'a': 1, 'b':2, 'c': 3}

# for k in d.keys():
#     print (k)

# for k in d.keys():
#     print (k)

# for key, val in d.items():
#     print (f"{key}-->{val}")


# construct from pairs
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

pair_dic = dict(zip(names, colors))
# print(pair_dic)

# COUNTING WITH DICTIONARIES

my_list = ['a', 'b', 'c', 'a', 'c', 'a']
# {'a': 3, 'b': 1, 'c': 2}

# from collections import default_dict, Counter()
# d = default_dict(int), 

counting_dict = {}
for num in my_list:
    # if (num not in counting_dict.keys()):
    #     counting_dict[num] = 0
    counting_dict[num] = counting_dict.get(num, 0) + 1
    # counting_dict[num] = counting_dict[num] + 1


print(counting_dict)