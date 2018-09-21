# Given a singly linked list, swap every two elements 
# (e.g. a->b->c->d->e->f->null should become b->a->d->c->f->e->null). 
# Code it such that memory position is swapped and not the node value.
# Bloomberg

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    # def print_(self):
    #     while self.next:
    #         print self.data
    #         self = self.next
 
# Use recursion
def swapNodes(head):
    if not head or not head.next:
        return head

    first = head
    second = head.next

    first.next = swapNodes(second.next)
    second.next = first

    return second
    
# No recursion
def swapNodes2(head):
    if not head or not head.next:
        return head

    fake = Node(0)
    fake.next = head
    cur = fake

    while cur.next and cur.next.next :

        tmp = cur.next.next
        cur.next.next = tmp.next
        tmp.next = cur.next
        cur.next = tmp
        cur = cur.next.next

    return fake.next

# head = Node(5,Node(3,Node(2)))
head = Node(5,Node(3,Node(2,Node(7,Node(10)))))
# n = swapNodes(head)
n = swapNodes2(head)
while n:
    print n.data
    n = n.next
# n.print_()
