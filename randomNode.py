import random

class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution(object):
    def __init__(self,head):
        self.head = head

    def getRandom(self):
        result = None
        cnt = 0
        node = self.head

        while node is not None :
            cnt += 1

            if cnt==1 :
                result = node
            else :
                k = int(random.random()*cnt)
                if k==1 :
                   result = node 
            node = node.next

        return result.data


node1 = ListNode(5)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(0)
node5 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution(node1)
print s.getRandom()
