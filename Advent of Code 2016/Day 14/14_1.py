import hashlib
import queue
import re

SALT = 'yjdafjpo'
hashes = {}
index = 0
keys_found = 0
test3 = re.compile(r"(.)\1\1")
while keys_found < 64:
    if index in hashes:
        hash = hashes[index]
    else:
        hash = hashlib.md5((SALT + str(index)).encode("utf-8")).hexdigest()
    match = test3.search(hash)
    if match:
        test_str = match.group(1) * 5
        test5 = re.compile(test_str)
        future_index = index
        while future_index < index + 1000:
            future_index += 1
            hash = hashlib.md5((SALT + str(future_index)).encode("utf-8")).hexdigest()
            hashes[future_index] = hash
            match = test5.search(hash)
            if match:
                keys_found += 1
                print(keys_found)
                break
    index += 1
print(index - 1)



