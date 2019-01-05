import sys

with open("input.txt") as inputFile:
    lines = inputFile.readlines()
place = 0
answer = ""
while place < len(lines[0]) - 1:
    charCount = [0] * 26
    for line in lines:
        charCount[ord(line[place]) - 97] += 1
    place += 1
    least = sys.maxsize
    leastIndex = 0
    for index, c in enumerate(charCount):
        if c < least and c != 0:
            leastIndex = index
            least = c
    answer += chr(leastIndex + 97)
print(answer)
