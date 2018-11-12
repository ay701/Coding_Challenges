# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its depth = 3.
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Use recursion. Each level's max depth: max(left_node, right_node)+1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_max_depth(node, max_depth):

    if node is None:
        return max_depth

    return max(find_max_depth(node.left, max_depth), find_max_depth(node.right, max_depth))+1


def find_min_depth(node, min_depth):

    if node is None:
        return min_depth

    return min(find_max_depth(node.left, min_depth), find_max_depth(node.right, min_depth))+1


n = Node(3)
n.left = Node(9)
n.right = Node(20)
n.right.left = Node(15)
n.right.right = Node(7)

print(find_max_depth(n, 0))
print(find_min_depth(n, 0))

