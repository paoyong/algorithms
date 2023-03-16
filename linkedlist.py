class Node:
    def __init__(self, prev, next, value):
        self.prev = prev
        self.next = next
        self.value = value

node1 = Node(None, None, 1)
node2 = Node(node1, None, 2)
node3 = Node(node2, None, 3)
node4 = Node(node3, None, 4)
node1.next = node2
node2.next = node3
node3.next = node4

def traverse(start):
    curr = start
    next = curr.next
    while(curr != None):
        print(curr.value)
        curr = next
        if (next != None):
            next = next.next

traverse(node1)
