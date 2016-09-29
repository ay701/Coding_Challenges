class Node:
    def __init__(self, data=None, nex=None):
    	self.data = data
    	self.next = nex

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
        print n, "is smaller than Linkedlist size: ", cnt
        exit

    return start


head = Node(2,Node(3,Node(4,Node(7))))
head = findlastNelements(head,1)
print head.data