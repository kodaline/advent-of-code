#!/usr/bin/env python3

#array = [3,8,1001,8,10,8,105,1,0,0,21,34,59,76,101,114,195,276,357,438,99999,3,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,102,4,9,9,101,2,9,9,102,4,9,9,1001,9,3,9,102,2,9,9,4,9,99,3,9,101,4,9,9,102,5,9,9,101,5,9,9,4,9,99,3,9,102,2,9,9,1001,9,4,9,102,4,9,9,1001,9,4,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99]

array = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

i = 0

# Split complex instructions which mix position and immediate mode, in an array of digits
def split(number):
    s = str(number)
    arr = [int(d) for d in s]
    if len(arr) < 4:
        arr = [0] + arr
    return arr

# Decode complex instructions which mix immediate and position modes, or default position
def decode_complex(content):
    global i
    num = split(content[i])
    #opcode = num[2:]
    #type_op1 = num[1]
    #type_op2 = num[0]
    one_two(content, num[3], mod=[num[1], num[0]])
    output(content, num[3], mod=[num[1]])
    if num[3] == 5:
        jump_if_true(content, mod=[num[1], num[0]])
    if num[3] == 6:
        jump_if_false(content, mod=[num[1], num[0]])
    if num[3] == 7:
        less_than(content, mod=[num[1], num[0]])
    if num[3] == 8:
        equals(content, mod=[num[1], num[0]])

# Opcode 4
def output(content, op, mod):
    global i
    type_op1 = mod
    op1 = content[i+1]
    if op == 4:
        print("DEBUGGING: ",op1)
        i += 2

# Opcode 5
def jump_if_true(content, mod=[0,0]):
    global i
    print("jump_if_true")
    op1 = content[i+1]
    op2 = content[i+2]
    posizione = content[i+3]
    type_op1, type_op2 = mod
    if type_op1 == 0:
        first = content[op1]
    else:
        first = op1
    if type_op2 == 0:
        second = content[op2]
    else:
        second = op2
    if first != 0:
        i = second
    else:
        i += 3
        return

# Opcode 6
def jump_if_false(content, mod=[0,0]):
    global i
    print("jump_if_false")
    op1 = content[i+1]
    op2 = content[i+2]
    posizione = content[i+3]
    type_op1, type_op2 = mod
    if type_op1 == 0:
        first = content[op1]
    else:
        first = op1
    if type_op2 == 0:
        second = content[op2]
    else:
        second = op2
    if first == 0:
        i = second
    else:
        i += 3
        return

# Opcode 7
def less_than(content, mod=[0,0]):
    global i
    print("less_than")
    op1 = content[i+1]
    op2 = content[i+2]
    posizione = content[i+3]
    type_op1, type_op2 = mod
    if type_op1 == 0:
        first = content[op1]
    else:
        first = op1
    if type_op2 == 0:
        second = content[op2]
    else:
        second = op2
    if first < second:
        content[posizione] = 1
        i += 4
    else:
        content[posizione] = 0
        i += 4

# Opcode 8
def equals(content, mod=[0,0]):
    global i
    print("equals")
    op1 = content[i+1]
    op2 = content[i+2]
    posizione = content[i+3]
    type_op1, type_op2 = mod

    if type_op1 == 0:
        first = content[op1]
    else:
        first = op1
    if type_op2 == 0:
        second = content[op2]
    else:
        second = op2
    if first == second:
        content[posizione] = 1
        i += 4
    else:
        content[posizione] = 0
        i += 4

# Opcodes 1 and 2
def one_two (content, op, mod=[0,0]):
    global i
    op1 = content[i+1]
    op2 = content[i+2]
    posizione = content[i+3]
    type_op1, type_op2 = mod
    if op == 1:
        somma = 0
        if type_op1 == 0:
            somma += content[op1]
        else:
            somma += op1
        if type_op2 == 0:
            somma += content[op2]
        else:
            somma += op2
        content[posizione] = somma
        i += 4
    if op == 2:
        prodotto = 1
        if type_op1 == 0:
            prodotto *= content[op1]
        else:
            prodotto *= op1
        if type_op2 == 0:
            prodotto *= content[op2]
        else:
            prodotto *= op2
        content[posizione] = prodotto
        i += 4

def get_input_position_first(array):
    i = 0
    for i in range(len(array)):
        if array[i] == 3:
            pos = i
            return pos

def get_input_position_second(array):
    i = 0
    flag = False
    for i in range(len(array)):
        if array[i] == 3:
            flag = True
        if flag == True:
            pos = i
            return pos

def input_opcode(copy_array, value, index):
    global i
    copy_array[copy_array[index+1]] = value
    i += 2

def output_opcode(content):
    global i
    i += 2
    return content[pos1]

# Manage the input array, based on the opcodes inside it
def calculate(content):
    global i
    l = len(content)
    while i <= l:
        if content[i] == 1:
            one_two(content, 1)
        elif content[i] == 2:
            one_two(content, 2)
        elif content[i] == 3:
            i+=2
        elif content[i] == 4:
            pos1 = content[i+1]
            i += 2
        elif content[i] == 5:
            jump_if_true(content)
        elif content[i] == 6:
            jump_if_false(content)
        elif content[i] == 7:
            less_than(content)
        elif content[i] == 8:
            equals(content)
        elif content[i] == 99:
            return content[0]
        else:
            decode_complex(content)
    print("valore",val)
    return content[pos1]

copy_array = array[:]
phase_setting = [4,3,2,1,0]
input_val = 0
j = 0
while j<5:
    copy_array[15] = phase_setting[j]
    copy_array[16] = input_val
    print(copy_array)
    print("array15", copy_array[15], "array16", copy_array[16])
    input_val = calculate(copy_array)
    print("input_val", input_val)
    print(copy_array)
    copy_array = array[:]
    j+=1
    i = 0
