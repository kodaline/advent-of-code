#!/usr/bin/env python3

import os

path = os.path.abspath('day6.txt')
fp = open(path, 'r')
array = []
for line in fp.readlines():
    line = line.rstrip()
    array.append(line)

fp.close()


