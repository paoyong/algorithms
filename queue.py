import unittest
from random import randint

class List:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        l = List(data)
        if self.head is None:
            self.tail = l
            self.head = l
            l.next = None
        else:
            l.next = self.tail
            self.tail = l

    def dequeue(self):
        h = self.head
        p = self.tail

        # Edge case of empty queue
        if h is None:
            return None

        # Edge case of one element
        if h is p:
            self.head = None
            self.tail = None
            return h.data

        # Find predecessor O(n)
        while p.next != h:
           p = p.next 

        self.head = p
        self.head.next = None

        traverse(self.tail)
        print("")
        return h.data

def traverse(l):
    if l is None:
        return 0
    else:
        print(l.data, end=" ")
        traverse(l.next)

class TestQueue(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        q.enqueue('John')
        q.enqueue('Sally')
        q.enqueue('Jenny')
        q.enqueue('Emma')
        q.enqueue('Sarah')
        q.enqueue('Pao')
        self.assertEqual(q.dequeue(), 'John')
        self.assertEqual(q.dequeue(), 'Sally')
        self.assertEqual(q.dequeue(), 'Jenny')
        self.assertEqual(q.dequeue(), 'Emma')
        self.assertEqual(q.dequeue(), 'Sarah')
        self.assertEqual(q.dequeue(), 'Pao')
        self.assertEqual(q.dequeue(), None)

    def test_big(self):
        q = Queue()
        lim = pow(2, 4)
        for i in range(1, lim):
            q.enqueue(randint(1, 100))

        for i in range(1, lim):
            q.dequeue()
        self.assertEqual(q.head, None)

if __name__ == '__main__':
    unittest.main()
