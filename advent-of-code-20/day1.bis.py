#!/usr/bin/env python3

import os
import math

path = os.path.abspath('day1.txt')

with open(path) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
val = 2020
content = [int(x) for x in content]
print(content)

for i in range(0,len(content)):
    for j in range(i,len(content)):
        for k in range(j,len(content)):

            if content[i] + content[j] + content[k] == val:
                print("The values are: ", content[i], content[j], content[k], "with result: ", content[i] * content[j] * content[k])
    

