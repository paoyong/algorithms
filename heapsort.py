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
    def young_child(self, i):
        # Case of where index 0 is given so it doesnt multiply by 0
        i = i + 1
        
        #if (i > self.n):
        #    return None

        return (2 * i) - 1

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
        print()

    # Given the index for the element in the array, bubble up that element satisfying heap dominance
    def bubble_up(self, i):
        p = self.parent(i)
        if p is None:
            return 0

        # Swap the > sign for min/max heap
        if self.q[i] < self.q[p]:
            self.swap(i, p)
            self.bubble_up(p)

    def bubble_down(self, i):
        min_index = i

        # Child index
        c = self.young_child(i)

        for j in range (0, 2):
            if (c + j) < self.n:
                if self.q[c + j] < self.q[min_index]:
                    min_index = c + j

        if min_index is not i:
            self.swap(min_index, i)
            self.bubble_down(min_index)

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

        # Move last element to first element
        self.q[0] = self.q[self.n - 1]
        self.q[self.n - 1] = None

        # Working with one less element now
        self.n = self.n - 1

        # Bubble down starting from root
        self.bubble_down(0)
        return min_value
        

# Sample tree to bubble down with
size = 20000
p = PriorityQueue(size)
for i in range(0, size):
    p.insert(random.randint(1, 100))
p.print_tree()
for i in range(0, size):
    print(p.extract_min())