import queue
import sys
import copy

class Node:
    def __init__(self, pos, steps, val):
        self.pos = pos
        self.steps = steps
        self.val = val

def get_neighbors(node, grid):
    x = node.pos[0]
    y = node.pos[1]
    neighbors = []
    if x > 0:
        neighbors.append(Node((x-1, y), node.steps + 1, grid[y][x-1]))
    if x < len(grid[0]) - 1:
        neighbors.append(Node((x+1, y), node.steps + 1, grid[y][x+1]))
    if y > 0:
        neighbors.append(Node((x, y-1), node.steps + 1, grid[y-1][x]))
    if y < len(grid) - 1:
        neighbors.append(Node((x, y+1), node.steps + 1, grid[y+1][x]))
    return [node for node in neighbors if node.val != "#"]

def print_grid(grid):
    for row in grid:
        print(row)

def BFS(start, goal, grid):
    if start.pos == goal:
        return 0
    q = queue.Queue()
    visited = set()
    q.put(start)

    while True:
        try:
            node = q.get(False)
            if node.pos in visited:
                continue
            visited.add(node.pos)
        except queue.Empty:
            print("no elements in queue")
            sys.exit(-1)
        else:
            if node.pos == goal:
                return node.steps
            neighbors = get_neighbors(node, grid)
            for neighbor in neighbors:
                if neighbor.pos not in visited:
                    q.put(neighbor)

def multiple_BFS(start, points_of_interest, order, grid):
    steps = []
    for item in order:
        goal = points_of_interest[item]
        steps.append(BFS(start, goal, grid))
    return steps

def build_permutations(string):
    if (len(string) == 1):
        return string
    permutations = []
    for letter in string:
        temp_string = string.copy()
        temp_string.remove(letter)
        lower_permutations = build_permutations(temp_string)
        for perm in lower_permutations:
            permutations.append(letter + perm)
    return permutations


grid = []
#read in file
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))

#find important coordinates
points_of_interest = {}
for row, line in enumerate(grid):
    for col, char in enumerate(line):
        if char not in ["#", "."]:
            points_of_interest[char] = (col, row)

for key, value in points_of_interest.items():
    x = value[0]
    y = value[1]
    grid[y][x] = "."

#generate the paths between all the nodes
path_lengths = []
points_of_interest_list = list(points_of_interest.keys())
points_of_interest_list.sort()
for item in points_of_interest_list:
    start = Node(points_of_interest[item], 0, item)
    steps = multiple_BFS(start, points_of_interest, points_of_interest_list, grid)
    path_lengths.append(steps)

points_of_interest_list.remove("0")
permutations = build_permutations(points_of_interest_list)
permutations = [list(x) for x in permutations]

min_steps = sys.maxsize
for permutation in permutations:
    steps = 0
    for index, item in enumerate(permutation[:-1]):
        i = int(item)
        j = int(permutation[index+1])
        steps += path_lengths[i][j]
    steps += path_lengths[0][int(permutation[0])]
    if steps < min_steps:
        min_steps = steps
        min_permutation = permutation

print("".join(min_permutation) + " " + str(min_steps))

