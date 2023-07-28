import math
import random

class PriorityQueue:
    def __init__(self, array_size):
        self.q = [None] * array_size

        # Number of elements
        self.n = 0

    # Return the queue (self.q) index of the parent node
    def parent(self, n):
        if (n == 0):
            return None
        
        return math.floor(n/2);

    # Return the queue (self.q) index of the left child node
    def young_child(self, n):
        if (n > self.n):
            return None

        return self.q[2 * n]

    # Given two indices for the queue, swap the elements of the two in the
    # array
    def swap(self, a, b):
        if a > self.n or b > self.n:
            raise Exception("Index doesn't exist. Out of bounds.")

        temp_a = self.q[a]
        self.q[a] = self.q[b]
        self.q[b] = temp_a

    # Binary Tree representation of the heap
    def print_tree(self):
        current_height = 0
        for i in range(0, self.n):
            prev_height = current_height
            current_height = math.floor(math.log(i + 1, 2)) + 1

            # Height change
            if prev_height is not current_height:
                print('')
                for a in range(0, self.n - (current_height * 2)):
                    print(' ', end="")

            print(self.q[i], end=" ")
        print("\nelements:", self.n)

    # Given the index for the element in the array, bubble up that element satisfying heap dominance
    def bubble_up(self, i):
        p = self.parent(i)
        if p is None:
            return 0

        # Swap the > sign for min/max heap
        if self.q[i] < self.q[p]:
            self.swap(i, p)
            self.bubble_up(p)

    # Given the index for an element in the array, find min of two children and potentially swap with
    # parent to reestablish dominance
    def bubble_down(self, i):
        p = self.parent(i)
        if p is None:
            return 0

        # Iterate over the two children
        for c in range (0, 1):
            if self.q[i - c - 1] < self.q[p]:
                self.swap(i - c - 1, p)

        # Recurse on the parent node to check that as well.
        # TODO
        self.bubble_down(p)

    # Heap Construction - bubble up on insert
    def insert(self, x):
        # Insert this new node first at the last empty slot in array
        self.q[self.n] = x

        # Bubble up this new element
        self.bubble_up(self.n)

        # Increase number of elements of our priority queue by 1
        self.n = self.n + 1

    def extract_min(self):
        min_value = self.q[0]
        self.q[0] = self.q[self.n - 1]
        self.q[self.n - 1] = None
        self.bubble_down(self.n - 1)
        return min_value
        

size = 10
p = PriorityQueue(size)
for i in range(0, size):
    p.insert(random.randint(1, 20))
p.print_tree()
print(p.extract_min())
p.print_tree()
