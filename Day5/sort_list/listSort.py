# sort a list in python

import random

list = []

for i in range(10):
    list.append(random.randrange(10))

print("Random generated list : ", list)

list.sort()
print("Sorted List : ", list)
