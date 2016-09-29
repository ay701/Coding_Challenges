# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

class Node:
    def __init__(self, data=None, nex=None):
    	self.data = data
    	self.next = nex

def addTwoLinkedlist(head1, head2):

    if head1 is None:
    	return head2

    if head2 is None:
    	return head1

    flag = 0
    fake = Node(0)
    cur = fake

    while head1 and head2:
        
        cur.next = Node(int((head1.data + head2.data + flag)%10))
        flag = int((head1.data + head2.data + flag)/10)
        head1 = head1.next
        head2 = head2.next
        cur = cur.next
 
    if head1:
        cur.next = head1

    if head2:
    	cur.next = head2

    return fake.next


head1 = Node(2,Node(4,Node(3)))
head2 = Node(5,Node(6,Node(4)))
head = addTwoLinkedlist(head1,head2)

while head:
	print head.data
	head = head.next


