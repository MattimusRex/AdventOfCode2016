import hashlib
inputStr = "cxdnnyjw"
index = 0
answer = [None] * 8
places = set()
count = 0
while count < 8:
    hashedStr = hashlib.md5((inputStr + str(index)).encode("utf-8")).hexdigest()
    if hashedStr[:5] == "00000":
        print(hashedStr)
        if hashedStr[5].isdigit():
            place = int(hashedStr[5])
            if place in range(0, 8) and place not in places:
                places.add(place)
                answer[place] = hashedStr[6]
                count += 1
                print(count)
    index += 1
print("".join(answer))