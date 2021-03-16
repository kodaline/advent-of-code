#!/usr/bin/env python3

import os
import math
import re
path = os.path.abspath('day3.txt')

with open(path) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
print(content)
free = 0
tree = 0
i = 3
for elem in content[1:]:
    if elem[i] == "#":
        tree += 1
    i = (i + 3)%len(elem)

print(tree)
