discs = [(1, 13), (10, 19), (2, 3), (1, 7), (3, 5), (5, 17)]
#discs = [(4, 5), (1, 2)]
time = 0

while True:
    win = True
    for i in range(1, len(discs) + 1):
        total_time = time + i
        pos = discs[i-1][0]
        num_of_slots = discs[i-1][1]
        if (pos + total_time) % num_of_slots != 0:
            win = False
            break
    if win:
        break
    else:
        time += 1
print(time)