import math

class PriorityQueue:
    def __init__(self, n):
        self.q = [None] * n
        self.n = n

    def parent(self, n):
        n = n - 1

        if (n is 1):
            return None
        
        return self.q[int(math.floor(n/2))];

    def young_child(self, n):
        if (n > self.n):
            return None

        n = n + 1
        return self.q[2 * n]
    
    # Heap Construction - bubble up on insert
    def insert(self, x):
        print(self.q)
        #if (x > self.q[self.n])
        


p = PriorityQueue(10)
p.q[0] = 1492
p.q[1] = 1783
p.q[2] = 1776
p.q[3] = 1804
p.q[4] = 1865
p.q[5] = 1945
p.q[6] = 1963
p.q[7] = 1918
p.q[8] = 2001
p.q[9] = 1941
p.insert(1300)

for a in p.q:
    print(a)

print('----')
print(p.parent(4))
print(p.young_child(4))
