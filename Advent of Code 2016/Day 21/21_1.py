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

def reverse(string, x, y):
    string[x:y+1] = reversed(string[x:y+1])

def move_pos(string, x, y):
    letter = string.pop(x)
    string.insert(y, letter)

input_string = ["a", "b", "c", "d", "e", "f", "g", "h"]
with open("input.txt") as f:
    for line in f:
        parts = line.split()
        if parts[0] == "swap" and parts[1] == "position":
            swap_pos(input_string, int(parts[2]), int(parts[5]))
        elif parts[0] == "swap" and parts[1] == "letter":
            swap_letter(input_string, parts[2], parts[5])
        elif parts[0] == "rotate" and parts[1] == "left":
            rotate_left(input_string, int(parts[2]))
        elif parts[0] == "rotate" and parts[1] == "right":
            rotate_right(input_string, int(parts[2]))
        elif parts[0] == "rotate" and parts[1] == "based":
            rotate_based_on(input_string, parts[6])
        elif parts[0] == "reverse":
            reverse(input_string, int(parts[2]), int(parts[4]))
        else:
            move_pos(input_string, int(parts[2]), int(parts[5]))
        #print(input_string)

print("".join(input_string))

