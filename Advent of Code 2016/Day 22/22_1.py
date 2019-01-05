class Node():
    def __init__(self, pos, size, used, avail):
        self.pos = pos
        self.size = size
        self.used = used
        self.avail = avail

    def print(self):
        print("Node: " + str(self.pos[0]) + "," + str(self.pos[1]))
        print("Size:  " + str(self.size))
        print("Used:  " + str(self.used))
        print("Avail: " + str(self.avail))
        print("")


with open("input.txt") as f:
    lines = f.readlines()

# make list of nodes from input file
nodes = []
for i in range(2, len(lines)):
    lines[i] = lines[i].split()
    node_pos = lines[i][0].split("-")
    node = Node((int(node_pos[1][1:]), int(node_pos[2][1:])), int(lines[i][1][:-1]), int(lines[i][2][:-1]), int(lines[i][3][:-1]))
    nodes.append(node)

pair_count = 0
#iterate through nodes, comparing all pairs
for i in range(len(nodes) - 1):
    for j in range(i+1, len(nodes)):
        if (nodes[i].used != 0 and nodes[i].used <= nodes[j].avail) or (nodes[j].used != 0 and nodes[j].used <= nodes[i].avail):
            pair_count += 1

print(pair_count)

