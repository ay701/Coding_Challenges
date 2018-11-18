# Given a singly linked list, swap every two elements 
# (e.g. a->b->c->d->e->f->null should become b->a->d->c->f->e->null). 
# Code it such that memory position is swapped and not the node value.
# Bloomberg
# https://www.youtube.com/watch?v=jiLloHVmLDc


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def print_(self):
        while self:
            print self.data
            self = self.next


# Change data, iter
def swap_nodes_iter(node):

    if node is None or node.next is None:
        return node

    head = node

    while node and node.next:

        tmp = node.data
        node.data = node.next.data
        node.next.data = tmp

        node = node.next.next

    return head


# Change data, recur
def swap_nodes_recur(node):

    if node is None or node.next is None:
        return node
    else:
        head = node
        tmp = node.data
        node.data = node.next.data
        node.next.data = tmp
        swap_nodes_recur(node.next.next)

    return head


# Change link, iter
def swap_nodes_iter2(node):

    if node is None or node.next is None:
        return node

    head = node.next

    while node and node.next:
        tmp = node.next.next
        node.next.next = node

        if tmp is not None and tmp.next is not None:
            node.next = tmp.next
        else:
            node.next = tmp

        node = tmp

    return head


# Change link, recur
def swap_nodes(head):
    if not head or not head.next:
        return head

    first = head
    second = head.next

    first.next = swap_nodes(second.next)
    second.next = first

    return second


# head = Node(5,Node(3,Node(2)))
head = Node(5)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(7)
head.next.next.next.next = Node(10)

n = swap_nodes_iter2(head)
# n = swap_nodes_recur(head)
n.print_()

