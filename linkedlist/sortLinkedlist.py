class Node:
    def __init__(self, data=None, nex=None):
    	self.data = data
    	self.next = nex

def sortLinkedlist(head):

    if head is None or head.next is None:
        return head

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
    	slow = slow.next
    	fast = fast.next.next

    right = sortLinkedlist(slow.next)
    slow.next = None
    left = sortLinkedlist(head)

    fake = Node(0)
    tail = fake

    while left is not None and right is not None:
    	if left.data < right.data:
            tail.next = left
            left = left.next
        else:
        	tail.next = right
        	right = right.next

        tail = tail.next

    if left is not None:
    	tail.next = left
    else:
    	tail.next = right

    return fake.next

head = sortLinkedlist(Node(4,Node(2,Node(5))))

while head is not None:
    print head.data
    head = head.next



