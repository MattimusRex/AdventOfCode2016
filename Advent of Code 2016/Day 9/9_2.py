import re

def count(text):
    pos = 0
    test = re.compile(r'\(\d+x\d+\)')
    charCount = 0
    while pos < len(text):
        marker = test.search(text, pos)
        if marker is None:
            for c in text[pos:]:
                charCount += 1
            pos = len(text)
        else:
            for c in text[pos:marker.start()]:
                charCount += 1
            parts = marker.group()[1:-1].split("x")
            substring = text[marker.end():marker.end() + int(parts[0])]
            charCount += count(substring) * int(parts[1])
            pos = marker.end() + int(parts[0])
    return charCount

with open("input.txt") as input_file:
    file_data = input_file.read().strip().replace(" ", "")
print(count(file_data))