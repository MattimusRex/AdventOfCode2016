with open("input.txt") as inputFile:
    #process strings
    lines = inputFile.readlines()
for line in lines:
    line = line[:len(line)-1]
    line = line.replace("[", "-")
    line = line.replace("]", "")
    parts = line.split("-")
    checksum = parts[-1]
    sectorID = parts[-2]
    encrypted = "".join(parts[:-2])
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
    #if real room, decrypt
    if checkString == checksum:
        shift = int(sectorID) % 26
        decrypted = ""
        for c in encrypted:        
            shiftedC = (((ord(c) - 97) + shift) % 26) + 97
            decrypted += chr(shiftedC)
        if "north" in decrypted:
            print(sectorID)
        
