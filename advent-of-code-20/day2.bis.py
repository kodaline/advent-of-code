#!/usr/bin/env python3

import os
import math
import re
path = os.path.abspath('day2.txt')

with open(path) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
content = [x.split(": ") for x in content]
count = 0
for elem in content:
    occ = elem[0]
    string = elem[1]
    occsplitted = occ.split(" ")    
    range_values = occsplitted[0].split("-")
    range_values = [int(x) for x in range_values]
    sub_string = occsplitted[1]
    if (string[range_values[0]-1] == sub_string and not string[range_values[1]-1] == sub_string) or (not(string[range_values[0]-1] == sub_string) and string[range_values[1]-1] == sub_string):
        print(range_values, sub_string, string)
        count+=1

print("Total passwords satisfying constraints: ", count)

    
