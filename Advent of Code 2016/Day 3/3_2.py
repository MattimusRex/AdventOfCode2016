count = 0
with open ("input.txt") as inputFile:
    lines = inputFile.readlines()
i = 0
while i < len(lines):
    parts = [lines[i].split()]
    parts.append(lines[i+1].split())
    parts.append(lines[i+2].split())
    triangles = [[parts[0][0], parts[1][0], parts[2][0]]]
    triangles.append([parts[0][1], parts[1][1], parts[2][1]])
    triangles.append([parts[0][2], parts[1][2], parts[2][2]])
    for triangle in triangles:
        tri = [int(side) for side in triangle]
        tri.sort()
        if tri[0] + tri[1] > tri[2]:
            count += 1
    i += 3
print(count)