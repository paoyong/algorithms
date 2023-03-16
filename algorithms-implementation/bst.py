import unittest
from random import randint

class Tree:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

def insert_tree(t, x, parent=None):
    if t is None:
        if x < parent.data:
            parent.left = Tree(x, parent, None, None)
        else:
            parent.right = Tree(x, parent, None, None)
        return 1

    if x < t.data:
        return insert_tree(t.left, x, t)
    else:
        return insert_tree(t.right, x, t)

# Tests
class TestTree(unittest.TestCase):
    def test_insert(self):
        root = Tree(10)
        insert_tree(root, 2)
        insert_tree(root, -8)
        insert_tree(root, 7)
        insert_tree(root, 12)
        insert_tree(root, 17)
        insert_tree(root, 11)
        self.assertEqual(root.left.data, 2)
        self.assertEqual(root.left.left.data, -8)
        self.assertEqual(root.left.right.data, 7)
        self.assertEqual(root.right.data, 12)
        self.assertEqual(root.right.left.data, 11)
        self.assertEqual(root.right.right.data, 17)

    def test_insert_large(self):
        num_nodes = pow(2,13)
        lim = 2000000000000
        root = Tree(lim)
        for i in range(1, num_nodes):
            insert_tree(root, randint(-lim, lim))
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
