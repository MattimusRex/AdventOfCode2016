import re
count = 0
with open("input.txt") as inputFile:
    #process each line, breaking into parts in brackets and parts outside of brackets
    for index, line in enumerate(inputFile):
        line = line.strip()
        notBracketParts = []
        bracketParts = []
        tempStr = ""
        for char in line:
            if char == '[':
                notBracketParts.append(tempStr)
                tempStr = ""
            elif char == ']':
                bracketParts.append(tempStr)
                tempStr = ""
            else:
                tempStr += char
        notBracketParts.append(tempStr)
        
        #if match not in brackets and no match in brackets, TLS
        TLS = False
        test = re.compile(r'(.)((?!\1).)\2\1')
        for part in notBracketParts:
            if test.search(part) is not None:
                TLS = True
                break
        for part in bracketParts:
            if test.search(part) is not None:
                TLS = False
                break
        if TLS:
            count += 1
print (count)
                
