with open("testInput.txt") as inputFile:
    lines = inputFile.readlines()
place = 0
answer = ""
while place < len(lines[0]) - 1:
    charCount = [0] * 26
    for line in lines:
        charCount[ord(line[place]) - 97] += 1
    place += 1
    answer += chr(charCount.index(max(charCount)) + 97)
print(answer)
