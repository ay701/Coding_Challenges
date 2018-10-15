# Input:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#   /
#  14
#
# Output: 2


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def min_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        depth = 0
        curr_level = [root]

        while curr_level:
            depth += 1
            next_level = []

            for n in curr_level:
                left = n.left
                right = n.right

                if left is None and right is None:
                    return depth

                if left:
                    next_level.append(left)

                if right:
                    next_level.append(right)

            curr_level = next_level

        return depth


if __name__ == "__main__":
    None

