# Insert a node to BST


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def insert(root, node):
    if root.data == node.data:
        root = node
    else:
        if node.data > root.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


node = Node(5)
insert(node)
