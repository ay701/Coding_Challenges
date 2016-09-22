def reverseLinkedlist(node):
    prev = None

    while node:
        nextnode = node.next
        node.next = prev
        prev = node
        node = nextnode

    return prev
