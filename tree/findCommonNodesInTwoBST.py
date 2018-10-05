# Print Common Nodes in Two Binary Search Trees
# Given two Binary Search Trees, find common nodes in them. In other words, find intersection of two BSTs.
# https://www.geeksforgeeks.org/print-common-nodes-in-two-binary-search-trees/


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def find_common_nodes_in_two_bst(n1, n2):

    output = []
    s1 = []
    s2 = []

    while True:

        if n1:
            s1.append(n1)
            n1 = n1.left
        elif n2:
            s2.append(n2)
            n2 = n2.left
        elif len(s1) and len(s2):
            n1 = s1[-1]
            n2 = s2[-1]
            # print(n1.data)
            # print(n2.data)

            if n1.data == n2.data:
                output.append(n1.data)

                s1.pop()
                s2.pop()

                n1 = n1.right
                n2 = n2.right
            elif n1.data < n2.data:
                s1.pop()
                n1 = n1.right
                n2 = None
            else:
                s2.pop()
                n2 = n2.right
                n1 = None
        else:
            break

    return output

node1 = Node(5)
node1.left = Node(1)
node1.right = Node(10)

node1.left.left = Node(0)
node1.left.right = Node(4)

node1.right.left = Node(7)
node1.right.left.right = Node(9)

node2 = Node(10)
node2.left = Node(7)
node2.right = Node(20)

node2.left.left = Node(4)
node2.left.right = Node(9)

print(find_common_nodes_in_two_bst(node1, node2))