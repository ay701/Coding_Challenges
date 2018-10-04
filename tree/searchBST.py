# search a node in BST 


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def search(root, node):
    if root.data == node.data:
        return root

    if root.data < node.data:
        return search(root.right)
    else:
        return search(root.left)

    return False
