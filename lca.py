def lca(root,x,y):
    if root is None or root==x or root==y:
        return root

    left = lca(root.left,x,y)
    right = lca(root.right,x,y)

    if left and right:
        return root

    if left:
        return left

    if right:
        return right

    return None


def lca_2(root,x,y):
    
    if root.data == x.data


def findPath(root,x):
    path = []
    stack = [] # keep right nodes

    while root or stack:

        if root:

            path.append(root)

            if root.data==x.data:
                return path

            stack.append(root.right)
            root = root.left 

        else:
            peek = stack[-1]

    findPath
