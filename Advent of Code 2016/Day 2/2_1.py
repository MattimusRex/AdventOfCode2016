current = 5
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        for c in line:
            if c == 'U':
                current = current - 3 if current - 3 > 0 else current
            elif c == 'D':
                current = current + 3 if current + 3 < 10 else current
            elif c == 'L':
                current = current - 1 if current not in [1, 4, 7] else current
            elif c == 'R': current = current + 1 if current not in [3, 6, 9] else current
        print(current)
