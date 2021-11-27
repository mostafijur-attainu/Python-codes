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
    
# Count total nodes
def TotalNodes(root):

    if root == None :
        return 0
    
    nodesL = TotalNodes(root.left)
    nodesR = TotalNodes(root.right)

    return nodesL + nodesR + 1

# Count height
def height(root):

    if root == None :
        return 0
    
    if root.left == None and root.right == None :
        return 0

    heightL = height(root.left)
    heightR = height(root.right)

    return max(heightL,heightR) + 1

# Left view
dic = {}
L = 1
def LeftView(root):
    global L

    if root == None :
        return

    if L not in dic :
        print(root.Data)
        dic[L] = 1
        
    L += 1
    LeftView(root.left)
    LeftView(root.right)
    L -= 1
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
