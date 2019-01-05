import hashlib
import queue
import re

def get_stretched_hash(SALT, index):
    hash = hashlib.md5((SALT + str(index)).encode("utf-8")).hexdigest()
    for i in range (0, 2016):
        hash = hashlib.md5((hash).encode("utf-8")).hexdigest()
    return hash

SALT = 'yjdafjpo'
hashes = {}
index = 0
keys_found = 0
test3 = re.compile(r"(.)\1\1")
while keys_found < 64:
    if index in hashes:
        hash = hashes[index]
    else:
        hash = get_stretched_hash(SALT, index)       
    match = test3.search(hash)
    if match:
        test_str = match.group(1) * 5
        test5 = re.compile(test_str)
        future_index = index
        while future_index < index + 1000:
            future_index += 1
            if future_index in hashes:
                hash = hashes[future_index]
            else:
                hash = get_stretched_hash(SALT, future_index)
                hashes[future_index] = hash
            match = test5.search(hash)
            if match:
                keys_found += 1
                print("key: " + str(keys_found) + " index: " + str(index))
                break
    index += 1
print(index - 1)



