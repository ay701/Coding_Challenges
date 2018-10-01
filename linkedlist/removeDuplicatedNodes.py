# Use hash, but hash doesn't guarantee the order, need to create another linkedlist
# O(N)
from collections import defaultdict

class Node:

    def __init__(self, data):
        self.data = data
        self.next_ = None


def remove_duplicated_nodes(node):

    if node is None or node.next_ is None:
        return node

    hash_ = defaultdict(lambda: False)
    node_ = node

    while node:
        data = node.data

        if not hash_.get(data):
            hash_[data] = True
            node_.next_ = node

        node = node.next_

    return node.next_

n = Node(5)
n.next_ = Node(7)
n.next_.next_ = Node(8)
n.next_.next_.next_ = Node(7)

remove_duplicated_nodes(n)

