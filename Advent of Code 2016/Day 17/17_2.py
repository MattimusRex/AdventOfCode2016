import hashlib
import queue

class Node():
    def __init__(self, pos, path):
        self.pos = pos
        self.path = path

OPEN = {"b", "c", "d", "e", "f"}
INITIAL_PASSCODE = "lpvhkcbi"

node = Node((0, 0), "")
nodes = queue.Queue()
nodes.put(node)
longest_path_length = 0

while True:
    try:
        node = nodes.get(False)
    except queue.Empty:
        print(longest_path_length)
        break
    else:
        pos = node.pos
        if pos == (3, 3):
            if longest_path_length < len(node.path):
                longest_path_length = len(node.path)
            continue
        hash = hashlib.md5((INITIAL_PASSCODE + node.path).encode("UTF-8")).hexdigest()
        #up
        if hash[0] in OPEN and pos[1] > 0:
            temp = Node((pos[0], pos[1] - 1), node.path + "U")
            nodes.put(temp)
        #down
        if hash[1] in OPEN and pos[1] < 3:
            temp = Node((pos[0], pos[1] + 1), node.path + "D")
            nodes.put(temp)
        #left
        if hash[2] in OPEN and pos[0] > 0:
            temp = Node((pos[0] - 1, pos[1]), node.path + "L")
            nodes.put(temp)
        #right
        if hash[3] in OPEN and pos[0] < 3:
            temp = Node((pos[0] + 1, pos[1]), node.path + "R")
            nodes.put(temp)
    

