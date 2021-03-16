#!/usr/bin/env python3
from functools import reduce
import os
import math
import sys
import re
path = os.path.abspath('day7.txt')

with open(path) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.split() for x in content]

def my_split(lista):
    key = ""
    result = []
    tokens = ["bag", "bags", "contain", "bag.", "bag,", "bags.", "bags,", "no", "other"]
    for elem in lista:
        if elem in tokens:
            if key:
                result.append(key)
                key = ""
        elif elem.isdigit():
            result.append(int(elem))
        else:
            key += elem
            
    return result

dict_res = {}
for i in content:
    result = my_split(i)
    dict_res[result[0]] = [(k,v) for v,k in zip(result[1::2], result[2::2])]
shinygold = dict_res["shinygold"]

i = 0
frontiera = set()
bags = ""
while i < len(shinygold):
    #import pudb; pu.db
    val = shinygold[i][0]
    if val in dict_res.keys() and val not in frontiera:
        bags += str(shinygold[i][1]) + "*"
        frontiera.add(val)
        shinygold.extend(dict_res[val])
    i += 1

print(containable)
