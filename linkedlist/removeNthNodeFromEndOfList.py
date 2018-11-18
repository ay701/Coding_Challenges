# LeetCode - Remove Nth Node From End of List (Python)
# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
#
# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example, given linked list 1->2->3->4->5 and n = 2, the result is 1->2->3->5.
#
#
# Method 1 (Use length of linked list)
# 1) Calculate the length of Linked List. Let the length be len.
# 2) Print the (len - n + 1)th node from the beginning of the Linked List.
#
# Time Complexity: O(n) where n is the length of linked list.
#
#
# Preferred -
# Method 2 (Use two pointers)
# Maintain two pointers - reference pointer and main pointer.
# Initialize both reference and main pointers to head.
# First move reference pointer to n nodes from head.
# Now move both pointers one by one until reference pointer reaches end.
# Now main pointer will point to nth node from the end. Return main pointer.
#
# Time Complexity: O(n) where n is the length of linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.nex = None


def remove_nth_node(head, n):

    first_node = head
    second_node = head.nex
    cnt = 1

    while second_node:
        if cnt < n:
            second_node = second_node.nex
            cnt += 1
            continue

        if cnt == n:
            first_node = first_node.nex
            second_node = second_node.nex
            continue

    return first_node.data


n = Node(2)
n.nex = Node(3)
n.nex.nex = Node(4)
n.nex.nex.nex = Node(5)
n.nex.nex.nex.nex = Node(6)
n.nex.nex.nex.nex.nex = Node(7)

print(remove_nth_node(n, 3))

