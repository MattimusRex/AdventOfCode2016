import re

string = "1T1223RS34CP4CPRST"
test = re.compile(r"\d[A-Z]*")
match = test.findall(string)  
print(match)