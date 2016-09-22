def hasCycle(node):

    if node==None or node.next==None:
        return False

    slow = node
    fast = node.next

    while slow or fast:
        slow = slow.next
        fast = fast.next.next
        
        if slow = fast:
            return True

    return False
