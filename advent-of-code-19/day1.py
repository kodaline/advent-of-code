#!/usr/bin/env python3

import os
import math


def fuel_required(val):
    val = math.floor(val/3.0) - 2
    return val

path = os.path.abspath('day1.txt')

with open(path) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
print(content)
val = 0
total = 0
for elem in content:
    val = math.floor(int(elem)/3.0) - 2
    while val > 0:
        total += val
        val = fuel_required(val)
    print(total)

