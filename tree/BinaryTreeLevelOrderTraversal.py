# https://shenjie1993.gitbooks.io/leetcode-python/102%20Binary%20Tree%20Level%20Order%20Traversal.html
#
# Input:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output:
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def binary_tree_level_order_traversal(self):

        if not self:
            return []

        result = [[self.data]]
        stack = [self]

        while stack:
            node = stack.pop(0)
            level_result = []

            if node.left:
                stack.append(node.left)
                level_result.append(node.left.data)

            if node.right:
                stack.append(node.right)
                level_result.append(node.right.data)

            if level_result:
                result.append(level_result)

        return result


node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)

print(node.binary_tree_level_order_traversal())
