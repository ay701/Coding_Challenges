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


def find_max_depth_binary_tree(node, max_):

    if node is None:
        return max_

    return max(find_max_depth_binary_tree(node.left, max_), find_max_depth_binary_tree(node.right, max_))+1


def find_min_depth_binary_tree(node, min_):

    if node is None:
        return min_

    min_ += 1

    if node.left is None and node.right is None:
        return min_

    return min(find_max_depth_binary_tree(node.left, min_), find_max_depth_binary_tree(node.right, min_))

n = Node(3)
n.left = Node(9)
n.right = Node(20)
n.right.left = Node(15)
n.right.right = Node(7)

print(find_max_depth_binary_tree(n, 0))
print(find_min_depth_binary_tree(n, 0))

