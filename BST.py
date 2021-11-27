# BST
def insert(root, data):

    if root == None :

        return Node(data)

    if data > root.Data :
        root.right = insert(root.right, data)

    elif data < root.Data :
        root.left = insert(root.left,data)

    return root

root = None

root = insert(root,7)
root = insert(root,2)
root = insert(root,3)
root = insert(root,8)
inOrder(root)
