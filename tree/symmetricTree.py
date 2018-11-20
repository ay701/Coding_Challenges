# Input:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# Output: True
#
# Input:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
# Output: False

# 解题思路
# 看一棵二叉树是否对称，就要首先看根节点的左右节点A和B是否有相同的值，如果A和B的值相等，
# 那么要继续判断A的左节点和B的右节点以及A的右节点和B的左节点是否对称，通过这样的方式来递归得到结果。
# 用迭代方法来解决的话，就把要判断是否对称的点按序（注意需要判断哪些节点是否相等）放到两个栈中，不断出栈和压栈来判断。
# AC源码


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Solve it recursively
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.is_symmetric(root.left, root.right)

    def is_symmetric(self, left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val != right.val:
            return False

        return self.is_symmetric(left.left, right.right) and self.is_symmetric(left.right, right.left)

    # Solve it iteratively
    # Using two stacks
    def is_symmetric_iterate(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack1, stack2 = [], []
        stack1.append(root.left)
        stack2.append(root.right)

        while stack1 and stack2:
            size1 = len(stack1)
            size2 = len(stack2)

            if size1 != size2:
                return False

            for __ in range(size1):
                curr1, curr2 = stack1.pop(), stack2.pop()

                if not curr1 and not curr2:
                    continue

                if not curr1 or not curr2:
                    return False

                if curr1.val != curr2.val:
                    return False

                stack1.append(curr1.left)
                stack1.append(curr1.right)
                stack2.append(curr2.right)
                stack2.append(curr2.left)

        return not stack1 and not stack2

if __name__ == "__main__":
    None
