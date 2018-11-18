# Use two pointers, one for head, another for end
# If counter equals to length of asked last n number, move both head and end pointer
# Otherwise move end pointer only
# Once end node's next is empty, terminate

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def findlastNelements(head,n):

    if head is None:
        return None

    cnt = 1
    start, end = head, head

    while end.next is not None:
        
        if cnt<n:
            end = end.next
            cnt += 1
        else:
            start = start.next
            end = end.next

    if cnt<n:
        print n, "is larger than Linkedlist size: ", cnt
        exit

    return start

head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(7)

head = findlastNelements(head,5)
print(head.data)