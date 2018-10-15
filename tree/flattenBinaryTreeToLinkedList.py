# https://www.programcreek.com/2013/01/leetcode-flatten-binary-tree-to-linked-list/
# Given a binary tree, flatten it to a linked list in-place.
#
# For example,
# Given
#
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# 
# The flattened tree should look like:
#
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Solution:
    def __init__(self, node):
        self.node = node

    def flatten_binary_tree_to_linked_list(self):
        if self.node is None:
            return None

        stack = []
        node = self.node

        while node:
            if node.right:
                stack.append(node.right)

            if node.left:
                node.right = node.left
                node.left = None
            elif len(stack):
                node.right = stack.pop()

            node = node.right

    def print_result(self):
        l = []

        while self.node:
            print str(self.node.data) + ""
            self.node = self.node.right


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(5)
node.left.left = TreeNode(3)
node.left.right = TreeNode(4)
node.right.right = TreeNode(6)

s = Solution(node)
s.flatten_binary_tree_to_linked_list()
s.print_result()
