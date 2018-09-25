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

def printLeftNode(root, curr_level, last_level):
    if root is None:
        return

    if last_level<curr_level:
        print "%d\t" %(root.data)
        last_level = curr_level

    curr_level += 1
    printLeftNode(root.left, curr_level, last_level)
    printLeftNode(root.right, curr_level, last_level)

def printLeftNodes(root):

    printLeftNode(root, 1, 0)




