# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def add_two_linked_list(head1, head2):

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    flag = 0
    fake = Node(0)
    cur = fake

    while head1 and head2:
        cur.next = Node(int((head1.data + head2.data + flag) % 10))
        flag = int((head1.data + head2.data + flag)/10)
        head1 = head1.next
        head2 = head2.next
        cur = cur.next

    while head1:
        cur.next = Node(int((head1.data + flag) % 10))
        flag = int((head1.data + flag)/10)
        head1 = head1.next
        cur = cur.next

    while head2:
        cur.next = Node(int((head2.data + flag) % 10))
        flag = int((head2.data + flag)/10)
        head2 = head2.next
        cur = cur.next

    if flag == 1:
        cur.next = Node(1)

    return fake.next


head1 = Node(2, Node(4, Node(3)))
head2 = Node(5, Node(6, Node(4)))
head = add_two_linked_list(head1, head2)


while head:
    print head.data
    head = head.next
