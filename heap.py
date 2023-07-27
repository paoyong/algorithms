import math

class PriorityQueue:
    def __init__(self, n):
        self.q = [None] * n
        self.n = n

    # Return the queue (self.q) index of the parent node
    def parent(self, n):
        if (n == 1):
            return None
        
        return self.q[int(math.floor(n/2))];

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

    # Heap Construction - bubble up on insert
    def insert(self, x):
        print(self.q)
        #if (x > self.q[self.n])

p = PriorityQueue(11)
p.q[0] = 5
p.q[1] = 3
p.q[2] = 8
p.q[3] = 1
p.q[4] = 2
p.q[5] = 6
p.q[6] = 9
p.q[7] = 4
p.q[8] = 7
p.print_tree()
