#!/usr/bin/env python3

#puzzle input: 171309-643603

from itertools import groupby
import numpy
from collections import Counter
from itertools import dropwhile
start = 171309
end = 643603

values = []

for i in range(start, end):
    values.append(i)

digits = []

for elem in values:
    digits.append([int(d) for d in str(elem)])


count = 0
lista = []
for elem in digits:
    if(all(elem[i] <= elem[i + 1] for i in range(len(elem)-1)) and (any(sum(1 for _ in g) > 1 for _, g in groupby(elem)) == True)):
        lista.append(elem)
"""
for elem in lista:
    if len(elem) < 6:
        lista.remove(elem)
"""

print(len(lista))

def unique(list1):
    # intilize a null list 
    unique_list = []
    # traverse for all elements 
    for x in list1:
        # check if exists in unique_list or not 
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

three = []
two = []
new_lista = []
for elem in lista:
    c = Counter(elem)
    for k,value in c.items():
        if value > 4:
            new_lista.append(elem)

unique_gfive = unique(new_lista)
print(len(new_lista))
print(len(unique_gfive))
lista = unique(lista)


four = []


for elem in lista:
    c = Counter(elem)
    for key, value in c.items():
        if value == 4:
            four.append(elem)
four = unique(four)
for elem in lista:
    c = Counter(elem)
    for key, value in c.items():
        if value == 3:
            three.append(elem)

counting = 0

new_four = []
new_three = []
three = unique(three)
for elem in three:
    c = Counter(elem)
    for key, value in c.items():
        if value == 2:
            new_three.append(elem)

used_three = []
unique_three = unique(new_three)

for elem in four:
    c = Counter(elem)
    for key, value in c.items():
        if value == 2:
            new_four.append(elem)


used_four = []
unique_four = unique(new_four)

print(len(lista) - len(unique_gfive) - (len(three)-len(unique_three)) - (len(four) - len(unique_four)))

