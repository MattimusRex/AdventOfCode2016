def move(curDir, xDist, yDist, visited, distance):
    if (curDir == 0):
        while distance > 0:
            yDist += 1
            distance -= 1
            if ((xDist, yDist)) in visited:
                return xDist, yDist, abs(xDist) + abs(yDist)
            visited.add((xDist, yDist))
    elif (curDir == 2):
        while distance > 0:
            yDist -= 1
            distance -= 1
            if ((xDist, yDist)) in visited:
                return xDist, yDist, abs(xDist) + abs(yDist)
            visited.add((xDist, yDist))
    elif (curDir == 1):
        while distance > 0:
            xDist += 1
            distance -= 1
            if ((xDist, yDist)) in visited:
                return xDist, yDist, abs(xDist) + abs(yDist)
            visited.add((xDist, yDist))
    else:
        while distance > 0:
            xDist -= 1
            distance -= 1
            if ((xDist, yDist)) in visited:
                return xDist, yDist, abs(xDist) + abs(yDist)
            visited.add((xDist, yDist))
    return xDist, yDist, -1

strInput = "L5, R1, L5, L1, R5, R1, R1, L4, L1, L3, R2, R4, L4, L1, L1, R2, R4, R3, L1, R4, L4, L5, L4, R4, L5, R1, R5, L2, R1, R3, L2, L4, L4, R1, L192, R5, R1, R4, L5, L4, R5, L1, L1, R48, R5, R5, L2, R4, R4, R1, R3, L1, L4, L5, R1, L4, L2, L5, R5, L2, R74, R4, L1, R188, R5, L4, L2, R5, R2, L4, R4, R3, R3, R2, R1, L3, L2, L5, L5, L2, L1, R1, R5, R4, L3, R5, L1, L3, R4, L1, L3, L2, R1, R3, R2, R5, L3, L1, L1, R5, L4, L5, R5, R2, L5, R2, L1, L5, L3, L5, L5, L1, R1, L4, L3, L1, R2, R5, L1, L3, R4, R5, L4, L1, R5, L1, R5, R5, R5, R2, R1, R2, L5, L5, L5, R4, L5, L4, L4, R5, L2, R1, R5, L1, L5, R4, L3, R4, L2, R3, R3, R3, L2, L2, L2, L1, L4, R3, L4, L2, R2, R5, L1, R2"
listInput = strInput.split(', ')
# N, E, S, W map 0, 1, 2, 3
curDir = 0
# 0, 2
xDist = 0
# 1, 3
yDist = 0
visited = set()
visited.add((0, 0))
for entry in listInput:
    direction = entry[0]
    distance = int(entry[1:])
    if (direction == "R"):
        curDir = 0 if curDir == 3 else curDir + 1
    else: 
        curDir = 3 if curDir == 0 else curDir - 1
    xDist, yDist, answer = move(curDir, xDist, yDist, visited, distance)
    if (answer != -1):
        print (answer)
        break

