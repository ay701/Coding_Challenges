# Print Left Nodes of a Binary Tree
# Given a binary tree, return the left-most node of each level in the tree.
# https://www.geeksforgeeks.org/print-left-view-binary-tree/
# Time Complexity: The function does a simple traversal of the tree, so the complexity is O(n).
#
# Input :
#                  1
#                /   \
#               2     3
#              / \     \
#             4   5     6
# Output : 1 2 4
#
# Input :
#         1
#       /   \
#     2       3
#       \
#         4
#           \
#             5
#              \
#                6
# Output :1 2 4 5 6

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printNode(root, curr_level, last_level):
    if root is None:
        return

    if last_level<curr_level:
        print "%d\t" %(root.data)
        last_level = curr_level

    curr_level += 1
    printNode(root.left, curr_level, last_level)
    printNode(root.right, curr_level, last_level)

def printLeftNodes(root):
    printNode(root, 1, 0)


# Driver program to test above function
root = Node(12)
root.left = Node(10)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)

printLeftNodes(root)


