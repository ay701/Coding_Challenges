# https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
# Python program to check if a binary tree is bst or not

INT_MAX = 4294967296
INT_MIN = -4294967296


# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Return true if the given tree is a BST and its values
# >= min and <= max
def is_bst(node, mini, maxi):
    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (is_bst(node.left, mini, node.data - 1) and
            is_bst(node.right, node.data + 1, maxi))


# Driver program to test above function
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

is_bst(root, INT_MIN, INT_MAX)

if is_bst(root):
    print "Is BST"
else:
    print "Not a BST"


