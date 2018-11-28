# LeetCode - Find Leaves of Binary Tree
#
#
# Given a binary tree, find all leaves and then remove those leaves.
# Then repeat the previous steps until the tree is empty.
#
# Example:
# Given binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Returns [4, 5, 3], [2], [1].
#
# Explanation:
# 1. Remove the leaves [4, 5, 3] from the tree
#
#           1
#          /
#         2
# 2. Remove the leaf [2] from the tree
#
#           1
# 3. Remove the leaf [1] from the tree
#
#           []

# https://segmentfault.com/a/1190000005938045
# https://github.com/criszhou/LeetCode-Python/blob/master/366.%20Find%20Leaves%20of%20Binary%20Tree.py
# Each index is it's level
# Make sure write helper function


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def find_leaves_helper(self, root, results):
        """
        push root and all descendants to results
        return the distance from root to farthest leaf
        """
        if not root:
            return -1

        ret = 1 + max(self.find_leaves_helper(child, results) for child in (root.left, root.right))

        if ret >= len(results):
            results.append([])

        results[ret].append(root.val)

        return ret

    def find_leaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        self.find_leaves_helper(root, ret)
        return ret


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)

print(Solution().findLeaves(node))
