#!/usr/bin/env python3

import os
import math
import sys
import re
path = os.path.abspath('day6.txt')

with open(path) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.split() for x in content]
j = 0
answers = []
cont = []
content.append([])
while j <= len(content)-1:
    while content[j] != []:
        answers.append(content[j])
        j += 1
    flat = [x for elem in answers for x in elem]
    answers = []
    cont.append(flat)
    j += 1
total = 0
for elem in cont:
    total += len(set("".join(elem)))

print(total)
