current = 5
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        for c in line:
            if c == 'U':
                if current in [10, 11, 12, 6, 7, 8]:
                    current -= 4
                elif current in [3, 13]:
                    current -= 2
            elif c == 'D':
                if current in [2, 3, 4, 6, 7 ,8]:
                    current += 4
                elif current in [1, 11]:
                    current += 2
            elif c == 'L':
                current = current - 1 if current not in [1, 2, 5, 10, 13] else current
            elif c == 'R': 
                current = current + 1 if current not in [1, 4, 9, 12, 13] else current
        print(current)