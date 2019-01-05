strInput = "L5, R1, L5, L1, R5, R1, R1, L4, L1, L3, R2, R4, L4, L1, L1, R2, R4, R3, L1, R4, L4, L5, L4, R4, L5, R1, R5, L2, R1, R3, L2, L4, L4, R1, L192, R5, R1, R4, L5, L4, R5, L1, L1, R48, R5, R5, L2, R4, R4, R1, R3, L1, L4, L5, R1, L4, L2, L5, R5, L2, R74, R4, L1, R188, R5, L4, L2, R5, R2, L4, R4, R3, R3, R2, R1, L3, L2, L5, L5, L2, L1, R1, R5, R4, L3, R5, L1, L3, R4, L1, L3, L2, R1, R3, R2, R5, L3, L1, L1, R5, L4, L5, R5, R2, L5, R2, L1, L5, L3, L5, L5, L1, R1, L4, L3, L1, R2, R5, L1, L3, R4, R5, L4, L1, R5, L1, R5, R5, R5, R2, R1, R2, L5, L5, L5, R4, L5, L4, L4, R5, L2, R1, R5, L1, L5, R4, L3, R4, L2, R3, R3, R3, L2, L2, L2, L1, L4, R3, L4, L2, R2, R5, L1, R2"
listInput = strInput.split(', ')
# N, E, S, W map 0, 1, 2, 3
curDir = 0
# 0, 2
xDist = 0
# 1, 3
yDist = 0
for entry in listInput:
    direction = entry[0]
    distance = int(entry[1:])
    if (direction == "R"):
        curDir = 0 if curDir == 3 else curDir + 1
    else: 
        curDir = 3 if curDir == 0 else curDir - 1
    if (curDir == 0):
        xDist += distance
    elif (curDir == 2):
        xDist -= distance
    elif (curDir == 1):
        yDist += distance
    else:
        yDist -= distance

print (abs(xDist) + abs(yDist))
