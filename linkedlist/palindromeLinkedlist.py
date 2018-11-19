# LeetCode - Palindrome Linked List (Python)
# Write a Function to check if a singly linked list is palindrome
# Given a singly linked list of characters, write a function that returns true if the given list is palindrome,
# else false.

# METHOD 1 (Use a Stack)
# A simple solution is to use a stack of list nodes. This mainly involves three steps.
# 1) Traverse the given list from head to tail and push every visited node to stack.
# 2) Traverse the list again. For every visited node, pop a node from stack and compare data of popped node with currently visited node.
# 3) If all nodes matched, then return true, else false.
#
# Time complexity of above method is O(n), but it requires O(n) extra space.
# Following methods solve this with constant extra space.
#
# METHOD 2 (By reversing the list)
# This method takes O(n) time and O(1) extra space.
# 1) We can use a fast and slow pointer to get the center of the list.
# 2) Reverse the second half of the linked list.
# 3) Check if the first half and second half are identical.
# 4) Construct the original linked list by reversing the second half again and attaching it back to the first half
#
# To divide the list in two halves, method 2 of this post is used.
# When number of nodes are even, the first and second half contain exactly half nodes.
# The challenging thing in this method is to handle the case when number of nodes are odd.
# We don't want the middle node as part of any of the lists as we are going to compare them for equality.
# For odd case, we use a separate variable 'midnode'.

# https://www.programcreek.com/2014/07/leetcode-palindrome-linked-list-java/
# https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/


class Node:
    def __init__(self, data):
        self.data = data
        self.nex = None

    def print_data(self):
        print(self.data)

        if self.nex:
            self.nex.print_data()


def is_palindrome(node):

    if not node or not node.nex:
        return True

    slow = node
    fast = node
    cnt = 0

    while True:
        if fast:
            cnt += 1
        else:
            break

        if fast.nex:
            cnt += 1
        else:
            break

        if fast and fast.nex:
            slow = slow.nex
            fast = fast.nex.nex
            continue

    if cnt % 2 == 1:
        second_node = slow.nex
    else:
        second_node = slow

    print(cnt)
    print(second_node.data)

    # reverse second part of list
    n1 = second_node
    n2 = n1.nex

    while n1 and n2:
        tmp = n2.nex
        n2.nex = n1
        n1 = n2
        n2 = tmp

    second_node.nex = None

    # compare 1st and 2nd list
    p1 = node
    p2 = n1 if n1 else n2

    print(p2.data, p1.data)

    while p1:
        print(p2.data)
        if p1.data != p2.data:
            print p1.data, p2.data
            return False

        p1 = p1.nex
        p2 = p2.nex

    return True


# driver code
n = Node(2)
n.nex = Node(3)
n.nex.nex = Node(4)
n.nex.nex.nex = Node(4)
n.nex.nex.nex.nex = Node(3)
n.nex.nex.nex.nex.nex = Node(2)

print(is_palindrome(n))
