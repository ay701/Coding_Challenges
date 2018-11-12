# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

# Python program to for tree traversals
# A class that represents an individual node in a
# Binary Tree


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def print_inorder(root):
    if root:
        # First recur on left child
        print_inorder(root.left)

        # then print the data of node
        print(root.val)

        # now recur on right child
        print_inorder(root.right)


# A function to do postorder tree traversal
def print_postorder(root):
    if root:
        # First recur on left child
        print_postorder(root.left)

        # the recur on right child
        print_postorder(root.right)

        # now print the data of node
        print(root.val)


# A function to do postorder tree traversal
def print_preorder(root):
    if root:
        # First print the data of node
        print(root.val),

        # Then recur on left child
        print_preorder(root.left)

        # Finally recur on right child
        print_preorder(root.right)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print "Preorder traversal of binary tree is"
print_preorder(root)

print "\nInorder traversal of binary tree is"
print_inorder(root)

print "\nPostorder traversal of binary tree is"
print_postorder(root)
