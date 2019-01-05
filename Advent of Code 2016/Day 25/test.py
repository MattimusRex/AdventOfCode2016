num = 2
while num <= 2572 or num % 2 == 1:
    if num % 2 == 0:
        num = (num * 2)  + 1
    else:
        num *= 2

print(num)