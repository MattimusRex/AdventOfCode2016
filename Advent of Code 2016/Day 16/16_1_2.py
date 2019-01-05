def dragon_curve(string):
    b = [string[x] for x in range(0, len(string))]
    b.reverse()
    b = ["0" if x == "1" else "1" for x in b]
    return string + "0" + "".join(b)
    

def calc_checksum(string):
    checksum = ""
    for i in range (0, len(string), 2):
        if string[i] == string[i+1]:
            checksum += "1"
        else:
            checksum += "0"
    return checksum


FILL_LENGTH = 35651584
INITIAL_STRING = "11110010111001001"

string = INITIAL_STRING
while len(string) < FILL_LENGTH:
    string = dragon_curve(string)
string = string[:FILL_LENGTH]

checksum = calc_checksum(string)
while len(checksum) % 2 == 0:
    checksum = calc_checksum(checksum)

print(checksum)