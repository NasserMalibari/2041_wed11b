#!/usr/bin/env python3

from collections import Counter, defaultdict, deque

my_list = [1,2,3,3,3,3,2]
c = Counter(my_list)
c[5] += 5

print(c)