import re

with open("input.txt") as input_file:
    file_data = input_file.read().strip().replace(" ", "")

pos = 0
test = re.compile(r'\(\d+x\d+\)')
result = ""
while pos < len(file_data):
    marker = test.search(file_data, pos)
    if marker is None:
        for c in file_data[pos:]:
            result += c
        pos = len(file_data)
    else:
        for c in file_data[pos:marker.start()]:
            result += c
        parts = marker.group()[1:-1].split("x")
        for i in range(0, int(parts[1])):
            for c in file_data[marker.end(): marker.end() + int(parts[0])]:
                result += c
        pos = marker.end() + int(parts[0])
print(len(result))
