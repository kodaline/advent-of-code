#!/usr/bin/env python3

import os
import math
import re
path = os.path.abspath('day4.txt')

with open(path) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.split() for x in content]
"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
lk = len(keys)
valid = 0
invalid = 0
j=0
cont = []
passports = []
content.append([])
while j <= len(content)-1:
    while content[j] != []:
        passports.append(content[j])
        j += 1
    flat = [x for elem in passports for x in elem]
    passports = []
    cont.append(flat)
    j += 1

print(cont)
for i in range(len(cont)):
    values = cont[i]
    k = [x.split(":")[0] for x in cont[i]]
    v = [x.split(":")[1] for x in cont[i]]
    if len(values) == lk:
        valid += 1
    elif len(values) == lk-1:
        if "cid" not in k:
            valid += 1
    else:
        invalid += 1
print(valid)
