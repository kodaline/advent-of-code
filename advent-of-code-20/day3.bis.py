#!/usr/bin/env python3

import os
import math
import re
path = os.path.abspath('day3.txt')

with open(path) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

def slopes(content, slope):
    tree = 0
    i = slope
    for elem in content[1:]:
        if elem[i] == "#":
            tree += 1
        i = (i + slope)%len(elem)
    return tree

def slopes_jump(content, slope, jump):
    tree = 0
    i = slope
    for elem in content[2::jump]:
        if elem[i] == "#":
            tree += 1
        i = (i + slope)%len(elem)
    return tree

tree1 = slopes(content,1)
tree3 = slopes(content,3)
tree5 = slopes(content,5)
tree7 = slopes(content,7)
tree_jump = slopes_jump(content,1,2)
print(tree1*tree3*tree5*tree7*tree_jump)
