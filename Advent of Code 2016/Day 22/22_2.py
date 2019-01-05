import queue
import sys

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

def get_neighbors(grid, node):
    x = node.pos[0]
    y = node.pos[1]
    neighbors = []
    if x > 0 and grid[y][x-1].used <= node.avail:
        neighbors.append(grid[y][x-1])
    if x < len(grid[0]) - 1 and grid[y][x+1].used <= node.avail:
        neighbors.append(grid[y][x+1])
    if y > 0 and grid[y-1][x].used <= node.avail:
        neighbors.append(grid[y-1][x])
    if y < len(grid) - 1 and grid[y+1][x].used <= node.avail:
        neighbors.append(grid[y+1][x])
    return neighbors

def print_grid(grid):
    print("   ", end="")
    for i in range(len(grid[0])):
        print("{:3d}".format(i), end=" ")
    print("")
    for index, row in enumerate(grid):
        print("{:3s}".format(str(index) + ":"), end="")
        for item in row:
            print("{:3d}".format(item.used), end=" ")
        print("")

with open("input.txt") as f:
    lines = f.readlines()


#make grid
nodes = []
for i in range(2, len(lines)):
    lines[i] = lines[i].split()
    node_pos = lines[i][0].split("-")
    x = int(node_pos[1][1:])
    y = int(node_pos[2][1:])
    #pos, size, used, avail
    node = Node((x, y), int(lines[i][1][:-1]), int(lines[i][2][:-1]), int(lines[i][3][:-1]))
    if int(lines[i][2][:-1]) == 0:
        empty = node
    if x == 0:
        nodes.append([node])
    else:
        nodes[y].append(node)

#need to move top right corner to the top left
#move blank to the left of top right, then move in circles to end
q = queue.Queue()
visited = set()
empty.count = 0
q.put(empty)
while True:
    try:
        node = q.get(False)
        node.used = 0
        node.avail = node.size
        print(node.pos)
        if node.pos == (nodes[0][-2].pos[0], 0):
            break
    except queue.Empty:
        print("broken")
        sys.exit(-1)
    else:
        neighbors = get_neighbors(nodes, node)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                neighbor.count = node.count + 1
                q.put(neighbor)

#now node to left of node we want
#1 move to move the goal 1 left
#then 5 moves per col
print((len(nodes[0][:-2]) * 5) + 1 + node.count)



