NUMBER_OF_ELVES = 3001330

def get_next_elf(presents, index):
    while presents[index] == 0:
        index += 1
        if index == len(presents):
            index = 0
    return index

presents = [1] * NUMBER_OF_ELVES
max = 0
i = 0
while True:
    #get the next elf with presents
    next_elf = get_next_elf(presents, 0) if i + 1 == len(presents) else get_next_elf(presents, i + 1)
    presents[i] += presents[next_elf]
    max = presents[i] if presents[i] > max else max
    if max == NUMBER_OF_ELVES:
        break
    presents[next_elf] = 0
    #get elf for next turn
    i = get_next_elf(presents, 0) if next_elf + 1 == len(presents) else get_next_elf(presents, next_elf + 1)
print(i + 1)
