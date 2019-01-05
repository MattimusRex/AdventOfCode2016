with open("input.txt") as inputFile:
    #process strings
    lines = inputFile.readlines()
total = 0
for line in lines:
    line = line[:len(line)-1]
    line = line.replace("[", "-")
    line = line.replace("]", "")
    parts = line.split("-")
    checksum = parts[-1]
    sectorID = parts[-2]
    encrypted = parts[:-2]
    charCounts = {}
    for part in encrypted:
        for c in part:
            if c in charCounts:
                charCounts[c] += 1
            else:
                charCounts[c] = 1
    
    #build strings check value
    check = []
    for i in range(5):
        max = 0
        for key, value in charCounts.items():
            if value > max:
                max = value
                char = key
            elif value == max:
                if key < char:
                    char = key
        check.append(char)
        charCounts[char] = 0

    checkString = ''.join(check)
    if checkString == checksum:
        total += int(sectorID)

print(total)
    

