# # You are given two linked lists representing two non-negative numbers. 
# # The digits are stored in reverse order and each of their nodes contain a single digit. 
# # Add the two numbers and return it as a linked list.
# # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# # Output: 7 -> 0 -> 8

def addTwoNumbers(m, n):

    fake = Node(0)
    p = fake
    flag = 0

    while m is not None and n is not None:
        sum_ = m.data + n.data + flag
        flag = sum_/10
        p.next = Node(sum_%10)
        m = m.next
        n = n.next
        p = p.next

    while m is not None:
        sum_ = m.data + flag
        flag = sum_/10
        p.next = Node(sum_%10)
        m = m.next
        p = p.next

    while n is not None:
        sum_ = n.data + flag
        flag = sum_/10
        p.next = Node(sum_%10)
        n = n.next
        p = p.next

    return fake.next
    

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def print_(self):
        while self:
            print self.data
            self = self.next

m = Node(5)
m.next = Node(3)
m.next.next = Node(1)
# m.print_()

n = Node(9)
n.next = Node(1)
n.next.next = Node(2)
# n.print_()

node = addTwoNumbers(m,n)
node.print_()
