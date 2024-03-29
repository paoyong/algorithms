import unittest
import sys
import io
from random import randint

class Tree:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

def search_tree(t, x):
    if t != None:
        if t.data is x:
            return t
        else:
            if x < t.data: 
                return search_tree(t.left, x)
            else:
                return search_tree(t.right, x)
    return None
    
def find_minimum(t):
    if t.left is None:
        return t.data
    else:
        return find_minimum(t.left)

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

def traverse_tree(t):
    if t != None:
        traverse_tree(t.left)
        print(t.data, end=" ")
        traverse_tree(t.right)

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

    def test_find_minimum(self):
        root = Tree(10)
        insert_tree(root, 2)
        insert_tree(root, -8)
        insert_tree(root, -9)
        insert_tree(root, 11)
        self.assertEqual(find_minimum(root), -9)

    def test_find_minimum_root_is_minimum(self):
        root = Tree(-15)
        insert_tree(root, 2)
        insert_tree(root, -8)
        insert_tree(root, -9)
        insert_tree(root, 11)
        self.assertEqual(find_minimum(root), -15)

    def test_find_minimum_one_node(self):
        root = Tree(-15)
        self.assertEqual(find_minimum(root), -15)

    def test_find_minimum_right_middle_node(self):
        root = Tree(5)
        insert_tree(root, -9)
        insert_tree(root, -9)
        insert_tree(root, -10)
        insert_tree(root, -9)
        self.assertEqual(find_minimum(root), -10)

    def test_traverse_tree(self):
        root = Tree(10)
        insert_tree(root, 2)
        insert_tree(root, -8)
        insert_tree(root, 7)
        insert_tree(root, 12)
        insert_tree(root, 17)
        insert_tree(root, 11)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        traverse_tree(root)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), '-8 2 7 10 11 12 17 ')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        insert_tree(root, 11)
        traverse_tree(root)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), '-8 2 7 10 11 11 12 17 ')

    def test_search_tree(self):
        root = Tree(10)
        insert_tree(root, 2)
        insert_tree(root, -8)
        insert_tree(root, 7)
        insert_tree(root, 12)
        insert_tree(root, 17)
        insert_tree(root, 11)
        self.assertEqual(search_tree(root, 12).data, 12)
        self.assertEqual(search_tree(root, 17).data, 17)
        self.assertEqual(search_tree(root, 24), None)

if __name__ == '__main__':
    unittest.main()
