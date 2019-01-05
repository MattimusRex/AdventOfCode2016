NUMBER_OF_ELVES = 3001330

class Node:
    def __init__(self, id, val, prev, next):
        self.id = id
        self.val = val
        self.prev = prev
        self.next = next

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.next

    def print(self):
        print("Node: " + str(self.id) + " Val: " + str(self.val))

#create circular linked list with head and end pointer
head = Node(1, 1, None, None)
end = head
for i in range (1, NUMBER_OF_ELVES):
    end.next = Node(i+1, 1, end, None)
    end = end.next
end.next = head

node_count = NUMBER_OF_ELVES
current = head
across = head
diff = 0
while True:
    distance = int(node_count / 2)
    
    #move to across elf
    while diff < distance:
        across = across.next
        diff += 1
    
    #take presents and remove from circle
    #moves forward one during delete, maintaining distance
    current.val += across.val
    if current.val == NUMBER_OF_ELVES:
        current.print()
        break
    across = across.delete()
    node_count -= 1

    current = current.next
    diff -= 1

