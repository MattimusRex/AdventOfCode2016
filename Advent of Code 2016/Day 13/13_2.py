import queue

MAGIC_NUMBER = 1358

class Node:
    def __init__(self, coor_pair, counter):
        self.pos = coor_pair
        self.counter = counter

def get_neighbors(node):
    if node.counter == 50:
        return []
    x = node.pos[0]
    y = node.pos[1]
    neighbors = []
    if x > 0:
        neighbors.append(Node((x-1, y), node.counter + 1))
    if y > 0:
        neighbors.append(Node((x, y-1), node.counter + 1))
    neighbors.append(Node((x+1, y), node.counter + 1))
    neighbors.append(Node((x, y+1), node.counter + 1))
    return [neighbor for neighbor in neighbors if not is_wall(neighbor.pos)]

def is_wall(coor_pair):
    x = coor_pair[0]
    y = coor_pair[1]
    n = (x*x + 3*x + 2*x*y + y + y*y) + MAGIC_NUMBER
    return bin(n).count("1") % 2 != 0

visited = set()
q = queue.Queue()
start_node = Node((1,1), 0)
q.put(start_node)
while True:
    try:
        node = q.get(False)
    except queue.Empty:
        break
    else:
        visited.add(node.pos)
        neighbors = get_neighbors(node)
        for neighbor in neighbors:
            if neighbor.pos not in visited:
                q.put(neighbor)
print(len(visited))