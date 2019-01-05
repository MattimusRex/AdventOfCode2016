lines = []
with open("input.txt") as f:
    for line in f:
        lines.append(line.replace("-", " ").split())
for i in range(len(lines)):
    lines[i] = [int(x) for x in lines[i]]

candidate = 0
blocked = True
while blocked:
    blocked = False
    for line in lines:
        if line[0] <= candidate and candidate <= line[1]:
            blocked = True
            candidate = line[1] + 1
            break
    
print(candidate)