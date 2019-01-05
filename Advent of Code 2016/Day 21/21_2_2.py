def swap_pos(string, x, y):
    temp = string[x]
    string[x] = string[y]
    string[y] = temp

def swap_letter(string, x, y):
    for i in range(len(string)):
        if string[i] == x:
            string[i] = y
        elif string[i] == y:
            string[i] = x

def rotate_left(string, steps):
    steps = steps % len(string)
    string.reverse()
    string[:-steps] = reversed(string[:-steps])
    string[-steps:] = reversed(string[-steps:])

def rotate_right(string, steps):
    steps = steps % len(string)
    string.reverse()
    string[:steps] = reversed(string[:steps])
    string[steps:] = reversed(string[steps:])

def rotate_based_on(string, x):
    index = string.index(x)
    steps = 2 + index if index >= 4 else 1 + index
    rotate_right(string, steps)

def rotate_based_on_reversed(string, x):
    index = string.index(x)
    if index == 0:
        rotate_left(string, 9)
    elif index == 1:
        rotate_left(string, 1)
    elif index == 2:
        rotate_left(string, 6)
    elif index == 3:
        rotate_left(string, 2)
    elif index == 4:
        rotate_left(string, 7)
    elif index == 5:
        rotate_left(string, 3)
    elif index == 6:
        rotate_left(string, 8)
    elif index == 7:
        rotate_left(string, 4)

def reverse(string, x, y):
    string[x:y+1] = reversed(string[x:y+1])

def move_pos(string, x, y):
    letter = string.pop(x)
    string.insert(y, letter)

def move_pos_reversed(string, x, y):
    letter = string.pop(y)
    string.insert(x, letter)

input_string = ['f', 'b', 'g', 'd', 'c', 'e', 'a', 'h']
with open("input.txt") as f:
    lines = f.readlines()
    
lines.reverse()    
for line in lines:
    parts = line.split()
    if parts[0] == "swap" and parts[1] == "position":
        swap_pos(input_string, int(parts[2]), int(parts[5]))
    elif parts[0] == "swap" and parts[1] == "letter":
        swap_letter(input_string, parts[2], parts[5])
    elif parts[0] == "rotate" and parts[1] == "left":
        rotate_right(input_string, int(parts[2]))
    elif parts[0] == "rotate" and parts[1] == "right":
        rotate_left(input_string, int(parts[2]))
    elif parts[0] == "rotate" and parts[1] == "based":
        rotate_based_on_reversed(input_string, parts[6])
    elif parts[0] == "reverse":
        reverse(input_string, int(parts[2]), int(parts[4]))
    else:
        move_pos_reversed(input_string, int(parts[2]), int(parts[5]))
print(input_string)

