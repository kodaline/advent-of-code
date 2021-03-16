#!/usr/bin/env python3

import os
import math
import re
path = os.path.abspath('day4.txt')

def check_height(val):
    least_cm = 150
    most_cm = 193
    least_in = 59
    most_in = 76
    if val[-2:] == "cm":
        return (int(val[:-2]) >= 150 and int(val[:-2]) <= 193)
    elif val[-2:] == "in":
        return (int(val[:-2]) >= 59 and int(val[:-2]) <= 76)
    else:
        #import pudb;pu.db
        return False
   
def check_hair_color(val):
    if val[0] != "#":
        return False
    else:
        return (re.findall(r"[0-9]|[a-f]",val[1:]) and len(val[1:]) == 6)

def check_pid(num):
    return (len(num) == 9 and num.isdigit())

def check_issue(num):
    least = 2010
    most = 2020
    return num.isdigit() and int(num) in range(least, most+1)

def check_expiration(num):
    least = 2020
    most = 2030
    return num.isdigit() and int(num) in range(least, most+1)

def check_birth(num):
    least = 1920
    most = 2002
    return num.isdigit() and int(num) in range(least, most+1)

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
ecl = ['amb','blu','brn','gry','grn','hzl','oth']

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

def check_eye_color(val):
    return (val in ecl)

func_dict = {
        "ecl": check_eye_color,
        "byr": check_birth,
        "iyr": check_issue,
        "eyr": check_expiration,
        "hgt": check_height,
        "hcl": check_hair_color,
        "pid": check_pid,
        }
checks = []
for i in range(len(cont)):
    check_invalid = False
    values = cont[i]
    k = [x.split(":")[0] for x in cont[i]]
    v = [x.split(":")[1] for x in cont[i]]
    #key,value together for check
    kv = [x.split(":") for x in cont[i]]
    if len(values) == lk:
        for key,value in kv:
            if key != "cid":
                if not func_dict[key](value):
                    invalid += 1
                    check_invalid = True
                    break
        if not check_invalid:
            valid += 1
    elif len(values) == lk-1 and "cid" not in k:
        for key,value in kv:
            if not func_dict[key](value):
                invalid += 1
                check_invalid = True
                break
        if not check_invalid:
            valid += 1
    else:
        invalid += 1
print(valid)

