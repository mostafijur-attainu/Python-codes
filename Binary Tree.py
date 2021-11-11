# Biary tree

def preOrder(root):

    if root == None :
        return
    
    print(root.Data)
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):

    if root == None :
        return
    
    inOrder(root.left)
    print(root.Data)
    inOrder(root.right)

class Node :

    def __init__(self, data):
        self.Data = data
        self.left = None
        self.right = None

root = None

Node1 = Node(1)
Node2 = Node(3)
Node3 = Node(5)
Node4 = Node(9)
Node5 = Node(7)

Node1.left = Node2
Node1.right = Node3
Node2.left = Node4
Node3.right = Node5

root = Node1
inOrder(root)
