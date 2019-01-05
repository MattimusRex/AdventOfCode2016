count = 0
with open ("input.txt") as inputFile:
    for line in inputFile:
        parts = line.split()
        intParts = []
        for part in parts:
            intParts.append(int(part))
        intParts.sort()
        if intParts[0] + intParts[1] > intParts[2]:
            count += 1
    print(count)