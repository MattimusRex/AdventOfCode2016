import hashlib
inputStr = "cxdnnyjw"
index = 0
answer = ""
while len(answer) < 8:
    hashedStr = hashlib.md5((inputStr + str(index)).encode("utf-8")).hexdigest()
    if hashedStr[:5] == "00000":
        print(str(index) + " " + hashedStr) 
        answer += hashedStr[5]
    index += 1
print(answer)
