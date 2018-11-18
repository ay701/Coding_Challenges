# Reverse a linked list
# Given pointer to the head node of a linked list, the task is to reverse the linked list.
# We need to reverse the list by changing links between nodes.
# https://www.geeksforgeeks.org/reverse-a-linked-list/
#
# Examples:
#
# Input : Head of following linked list
#        1->2->3->4->NULL
# Output : Linked list should be changed to,
#        4->3->2->1->NULL
#
# Input : Head of following linked list
#        1->2->3->4->5->NULL
# Output : Linked list should be changed to,
#        5->4->3->2->1->NULL
#
# Input : NULL
# Output : NULL
#
# Input  : 1->NULL
# Output : 1->NULL


class Node:
    def __init__(self, data):
        self.data = data
        self.nex = None

    def print_data(self):
        print(self.data)

        if self.nex:
            self.nex.print_data()


def reverse_linked_list(node):
    prev = None

    while node:
        next_node = node.nex
        node.nex = prev
        prev = node
        node = next_node

    return prev


def rev_linked_list(head):

    if head is None or head.nex is None:
        return head

    prev = None
    cur = head

    while cur:
        nex = cur.nex
        cur.nex = prev
        prev = cur
        cur = nex

    return prev


# driver code
n = Node(2)
n.nex = Node(3)
n.nex.nex = Node(4)
n.nex.nex.nex = Node(5)
n.nex.nex.nex.nex = Node(6)
n.nex.nex.nex.nex.nex = Node(7)

reverse_linked_list(n).print_data()
rev_linked_list(n).print_data()

