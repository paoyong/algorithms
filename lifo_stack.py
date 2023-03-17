import unittest

class LIFOStack:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.array = [None] * size

    def push(self, data):
        self.array[self.count] = data
        self.count += 1
        
    def pop(self):
        r = self.array[self.count - 1]
        self.array[self.count - 1] = None
        self.count -= 1
        return r

class TestLIFOStack(unittest.TestCase):
    def test_push(self):
        s = LIFOStack(10)
        s.push(1)
        s.push(3)
        s.push(7)
        s.push(5)
        self.assertEqual(s.array[0], 1)
        self.assertEqual(s.array[1], 3)
        self.assertEqual(s.array[2], 7)
        self.assertEqual(s.array[3], 5)

    def test_pop(self):
        s = LIFOStack(10)
        s.push(1)
        s.push(3)
        s.push(7)
        s.push(5)
        self.assertEqual(s.pop(), 5)
        self.assertEqual(s.pop(), 7)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 1)

        for i in range(1, 10):
            self.assertEqual(s.array[i], None)

if __name__ == '__main__':
    unittest.main()