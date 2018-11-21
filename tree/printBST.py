# Print left-most node of each level


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def traverse(root):

    cur_level = [root]

    while cur_level:
        next_level = []

        for node in cur_level:
            print node.value

            if node.left:
                next_level.append(node.left)

            if node.right:
                next_level.append(node.right)

        cur_level = next_level
       

# Use queue, breadth-first search, find node
def traverse_bfs(root):
    
    queue = [root]

    while queue:
        node = queue.pop(0)
        print node.value
        # if node.value == val:
        #    return True

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    # return False


# Use stack, depth-first search, find node
def traverse_dfs(root):
    stack = [root]

    while queue:
        node = stack.pop()
        print node.value
        # if node.value == val:
        #    return True

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


t = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))
traverse(t)
traverse_bfs(t)
traverse_dfs(t)