import sys

def copy(x, y, registers):
    if str.isdigit(x):
        registers[y] = int(x)
    else:
        registers[y] = int(registers[x])

def increment(x, registers):
    registers[x] += 1

def decrement(x, registers):
    registers[x] -= 1

def jump_not_zero(x, y, registers):
    if str.isdigit(x) and int(x) != 0:
        return int(y) - 1
    elif not str.isdigit(x) and registers[x] != 0:
        return int(y) - 1
    else:
        return 0

registers = {"a":0, "b":0, "c":0, "d":0}
counter = 0
with open("input.txt") as f:
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
    else:
        print("Invalid command: " + lines[i][0] + ", exiting")
        sys.exit(1)
    counter += 1
    if counter % 100 == 0:
        print(counter)
    i += 1
print(registers["a"])