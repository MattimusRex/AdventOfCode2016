def printScreen(screen):
    for row in screen:
        print("".join(row))

def rect(dimensions, screen):
    parts = dimensions.split("x")
    for row in screen[:(int(parts[1]))]:
        for index, pixel in enumerate(row[:int(parts[0])]):
            row[index] = "0"

def rotateRow(row, distance):
    newRow = [0] * len(row)
    distance = int(distance)
    i = 0
    j = len(newRow) - distance
    while i < len(newRow):
        newRow[i] = row[j % len(newRow)]
        i += 1
        j += 1
    return newRow

def rotateCol(col, cIndex, distance, screen):
    col = rotateRow(col, distance)
    for index, row in enumerate(screen):
        row[cIndex] = col[index]

def getCol(cIndex, screen):
    newCol = []
    for row in screen:
        newCol.append(row[cIndex])
    return newCol
    
screen = []
for i in range(0, 6):
    screen.append(["."]*50)
with open("input.txt") as inputFile:
    for line in inputFile:
        #['rotate', 'row', 'y=1', 'by', '10']
        #['rotate', 'column', 'x=48', 'by', '4']
        #['rect', '9x1']
        parts = line.split()
        if parts[0] == "rect":
            rect(parts[1], screen)
        elif parts[1] == "row":
            rIndex = int(parts[2].split("=")[1])
            row = screen[rIndex]
            screen[rIndex] = rotateRow(row, parts[4])
        else:
            cIndex = int(parts[2].split("=")[1])
            col = getCol(cIndex, screen)
            rotateCol(col, cIndex, parts[4], screen)

printScreen(screen)
            