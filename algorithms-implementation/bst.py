class Tree:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

def insert_tree(t, x, parent):
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

# Sample data
root = Tree(10)
insert_tree(root, 2, None)
insert_tree(root, 12, None)
insert_tree(root, 17, None)
insert_tree(root, 11, None)
print(root.left.data)
print(root.right.left.data)
