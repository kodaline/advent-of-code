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
            pass
        else:
            key += elem
            
    return result

dict_res = {}
for i in content:
    result = my_split(i)
    dict_res[result[0]] = result[1:]

desired = "shinygold"
containable = 0
for k,v in dict_res.items():
    i = 0
    frontiera = set()
    if k == desired:
        continue
    else:
        while i < len(v):
            #import pudb; pu.db
            val = v[i]
            if val == desired:
                containable += 1
                break
            if val in dict_res.keys() and val not in frontiera:
                frontiera.add(val)
                v.extend(dict_res[val])
            i += 1

print(containable)
