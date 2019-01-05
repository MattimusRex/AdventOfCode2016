import sys
import copy as c

def add(x, y, registers):
    if y in registers:
        y = registers[y]
    else:
        y = int(y)
    registers[x] += y

def copy(x, y, registers):
    if x not in registers and y in registers:
        registers[y] = int(x)
    elif y in registers:
        registers[y] = int(registers[x])

def divide(x, y, registers):
    if y in registers:
        y = registers[y]
    else:
        y = int(y)
    registers[x] = int(registers[x] / y)

def increment(x, registers):
    if x in registers:
        registers[x] += 1

def decrement(x, registers):
    if x in registers:
        registers[x] -= 1

def jump_not_zero(x, y, registers):
    if y not in registers:
        y = int(y)
    else:
        y = registers[y]
    if x not in registers:
        x = int(x)
    else:
        x = registers[x]
    if x != 0:
        return y - 1
    else:
        return 0

def multiply(x, y, registers):
    if y in registers:
        y = registers[y]
    else:
        y = int(y)
    registers[x] = registers[x] * y

def toggle(line):
    cmd = line[0]
    if cmd == "inc":
        line[0] = "dec"
    elif cmd == "dec":
        line[0] = "inc"
    elif cmd == "tgl":
        line[0] = "inc"
    elif cmd == "jnz":
        line[0] = "cpy"
    elif cmd == "cpy":
        line[0] = "jnz"
    return line

def out(x):
    if x in registers:
        x = registers[x]
    else:
        x = int(x)
    return x

def reset(registers, starting_a):
    registers = registers.fromkeys(registers, 0)
    i = 0
    prev = None
    starting_a += 1
    registers["a"] = starting_a
    return i, prev, starting_a, registers


registers = {"a":2572, "b":0, "c":0, "d":2572}
starting_a = 158
registers["a"] += starting_a
registers["d"] += starting_a
prev = None
counter = 0
with open("modified_input.txt") as f:
    lines = f.readlines()
lines = [x.split() for x in lines]
i = 0
while i < len(lines):
    if lines[i][0] == "cpy":
        copy(lines[i][1], lines[i][2], registers)
    elif lines[i][0] == "inc":
        increment(lines[i][1], registers)
    elif lines[i][0] == "dec":
        decrement(lines[i][1], registers)
    elif lines[i][0] == "jnz":
            i += jump_not_zero(lines[i][1], lines[i][2], registers)
    elif lines[i][0] == "tgl":
        x = lines[i][1]
        if not str.isdigit(x):
            x = registers[x]
        else:
            x = int(x)
        if i+x > -1 and i+x < len(lines):
            lines[i+x] = toggle(lines[i+x])
    elif lines[i][0] == "mul":
        multiply(lines[i][1], lines[i][2], registers)
    elif lines[i][0] == "out":
        x = out(lines[i][1])
        print(x)
        if x not in [0, 1] or (prev != None and x == prev):
            i, prev, starting_a, registers = reset(registers, starting_a)
    elif lines[i][0] == "add":
        add(lines[i][1], lines[i][2], registers)
    elif lines[i][0] == "div":
        divide(lines[i][1], lines[i][2], registers)
    else:
        print("Invalid command: " + lines[i][0] + ", exiting")
        sys.exit(1)
    counter += 1
    i += 1
print(registers["a"])