# Linked lists

class Node:

    def __init__(self, data):
        self.Data = data
        self.Next = None


# Node1 =  Node(1)
# Node2 =  Node(6)
# Node3 =  Node(5)
# Node4 =  Node(2)

# Node1.Next = Node2
# Node2.Next = Node3
# Node3.Next = Node4

# Head = Node1
# Temp = Head

# while Temp != None:
#     print(Temp.Data, end = " ")
#     Temp = Temp.Next

# Inserting at 3rd position
# Temp = Head
# curr = 1

# print()
# while curr != 2:
#     Temp = Temp.Next
#     curr +=1

# NodeIns = Node(3)
# print(NodeIns)
# NodeIns.Next = Temp.Next
# Temp.Next = NodeIns

# Temp = Head
# while Temp != None:
#     print(Temp.Data, end = " ")
#     Temp = Temp.Next
# print()

# Insertion at last node

# Node1 =  Node(1)
# Node2 =  Node(2)
# Node3 =  Node(3)
# Node4 =  Node(4)

# Node1.Next = Node2
# Node2.Next = Node3
# Node3.Next = Node4

# Head = Node1
# Temp = Head
# while Temp != None:
#     print(Temp.Data, end = " ")
#     Temp = Temp.Next
# print()
# NodeIns = Node(5)
# Temp = Head
# while Temp.Next != None :

#     Temp = Temp.Next

# Temp.Next = NodeIns
# Temp = Head
# while Temp != None:
#     print(Temp.Data, end = " ")
#     Temp = Temp.Next
# print()

# Delete 3rd node

# Node1 =  Node(1)
# Node2 =  Node(2)
# Node3 =  Node(3)
# Node4 =  Node(4)

# Node1.Next = Node2
# Node2.Next = Node3
# Node3.Next = Node4

# Head = Node1
# Temp = Head
# while Temp != None:
#     print(Temp.Data, end = " ")
#     Temp = Temp.Next
# print()

# curr = Head
# prev = None

# pos = 1

# while pos!= 3:

#     prev = curr
#     curr = curr.Next
#     pos +=1

# prev.Next = curr.Next
# curr.Next = None
# del curr

# Temp = Head
# while Temp != None:
#     print(Temp.Data, end = " ")
#     Temp = Temp.Next
# print()

