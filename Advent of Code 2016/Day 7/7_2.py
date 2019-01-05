def findAllMatches(test, part):
    results = []
    position = 0
    while True:
        match = test.search(part, position)
        if match is None:
            return results
        results.append(match.group())
        position = match.start() + 1
    return results

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
        
        #find ABA out of brackets
        #if ABA, find BAB in brackets
        #if BAB, true  
        SSL = False
        test = re.compile(r'(.)(?!\1).\1')
        for part in notBracketParts:
            matches = findAllMatches(test, part)
            for match in matches:
                tempStr = match[1] + match[0] + match[1]
                for part in bracketParts:
                    if tempStr in part:
                        SSL = True
        if SSL:
            count += 1
print (count)
                
