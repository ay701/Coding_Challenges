def reverse_linked_list(node):
    prev = None

    while node:
        next_node = node.next
        node.next = prev
        prev = node
        node = next_node

    return prev

def rev_linked_list(head):

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
