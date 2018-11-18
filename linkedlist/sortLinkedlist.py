class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sort_linked_list(head):

    if not head or not head.next:
        return head

    slow = head
    fast = head.next

    while not fast and not fast.next:
        slow = slow.next
        fast = fast.next.next

    right = sort_linked_list(slow.next)
    slow.next = None
    left = sort_linked_list(head)

    fake = Node(0)
    tail = fake

    while not left and not right:
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


head = sort_linked_list(Node(4, Node(2, Node(5))))

while head is not None:
    print head.data
    head = head.next



