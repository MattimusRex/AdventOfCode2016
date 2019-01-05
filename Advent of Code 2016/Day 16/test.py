string = "111100010101"
b = [string[x] for x in range(0, len(string))]
b.reverse()
print(b)
b = ["0" if x == "1" else "1" for x in b]
print(b)