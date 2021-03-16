#!/usr/bin/env python3

import os
import math
import sys
import re
path = os.path.abspath('day5.txt')

with open(path) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.split() for x in content]
print(content)

ticket = -sys.maxsize

for i in range(len(content)):

    #import pudb;pu.db 
    row_chars = content[i][0][:7]
    col_chars = content[i][0][7:]
    row_start = 0
    row_end = 127
    col_start = 0
    col_end = 7
    for i in range(len(row_chars)):
        val = row_chars[i]
        if val == "F":
            row_end = (row_end+row_start)//2
        elif val == "B":
            row_start = (row_end+row_start+1)//2
    row = row_end
    for val in col_chars:
        if val == "L":
            col_end = (col_end+col_start)//2
        elif val == "R":
            col_start = (col_end+col_start+1)//2
    col = col_end
    print(row,col)
    ticket_id = row*8 + col
    if ticket_id > ticket:
        ticket = ticket_id

print(ticket)
    

