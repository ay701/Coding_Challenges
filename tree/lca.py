# Lowest Common Ancestor
# http://www.crazyforcode.com/lowest-common-ancestor-binary-tree/
# https://www.youtube.com/watch?v=13m9ZCB8gjw


def lca(root, x, y):
    if root is None or root == x or root == y:
        return root

    left = lca(root.left, x, y)
    right = lca(root.right, x, y)

    if left and right:
        return root

    if left:
        return left

    if right:
        return right

    return None


# A recursive python program to find LCA of two nodes
# n1 and n2

# A Binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca(root, n1, n2):
    # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if root.data > n1 and root.data > n2:
        return lca(root.left, n1, n2)

        # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if root.data < n1 and root.data < n2:
        return lca(root.right, n1, n2)

    return root


def find_path(root, x):
    path = []
    stack = [] # keep right nodes

    while root or stack:

        if root:
            path.append(root)

            if root.data == x.data:
                return path

            stack.append(root.right)
            root = root.left 

        else:
            peek = stack[-1]

        # find_path
