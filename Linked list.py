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
# Reverse a linked list

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
# print()

# CURR = Node1
# PREV = None

# while CURR != None:

#     NEXT = CURR.Next
#     CURR.Next = PREV
#     PREV = CURR
#     CURR = NEXT

# Temp = PREV
# while Temp != None:
#     print(Temp.Data, end = " ")
#     Temp = Temp.Next
# print()

# Linked list cycle 

Node1 =  Node(1)
Node2 =  Node(6)
Node3 =  Node(5)
Node4 =  Node(2)

Node1.Next = Node2
Node2.Next = Node3
Node3.Next = Node4
Node4.Next = Node2

Head = Node1
Temp = Head

dic = {}
ans = False

while Temp != None:

    if Temp not in dic :
        dic[Temp] = 1
    
    else:
        dic[Temp] += 1
    
    print(Temp, Temp.Data)
    if dic[Temp] > 1:
        ans = True
        break
    
    Temp = Temp.Next

print(dic)
print(ans)


# Linked list cycle - Fast and slow pointer

# Node1 =  Node(1)
# Node2 =  Node(6)
# Node3 =  Node(5)
# Node4 =  Node(2)
# Node5 =  Node(7)

# Node1.Next = Node2
# Node2.Next = Node3
# Node3.Next = Node4
# Node4.Next = Node5
# Node5.Next = Node1

# Head = Node1

# if Head  = None :
#     print(False)
# else:
#     slow = Head
#     fast = Head.Next

#     ans = False

#     while slow.Next != None and fast.Next != None and fast.Next.Next != None and slow != fast :
#         slow = slow.Next
#         fast = fast.Next.Next

#     if slow == fast:
#         ans = True

# print(ans)
