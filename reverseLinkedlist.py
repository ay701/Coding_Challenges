def reverseLinkedlist(node):
    prev = None

    while node:
        nextnode = node.next
        node.next = prev
        prev = node
        node = nextnode

    return prev

def revLinkedlist(head):

    if head is None or head.next is None:
        return head

    prev = None
    cur = head

    while cur is not None:
        nex = cur.next 
        cur.next = prev
        prev = cur
        cur = nex

    return prev
