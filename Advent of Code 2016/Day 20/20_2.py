lines = []
with open("input.txt") as f:
    for line in f:
        lines.append(line.replace("-", " ").split())

lows = []
highs = []
for line in lines:
    lows.append(int(line[0]))
    highs.append(int(line[1]))

lows.sort()
highs.sort()
count = 0
lower_boundary = 0
for i in range(len(lows)):
    diff = lows[i] - lower_boundary - 1
    if diff  > 0:
        count += diff
    lower_boundary = highs[i]
print(count)
