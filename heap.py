import heapq
# Min Heap
# h = [3, 6, 5, 7, 4, 2, 8]
# print(h)
# heapq.heapify(h)
# print(h)
# heapq.heappush(h,9)
# heapq.heappush(h,3)
# print(h)

# print(heapq.heappop(h))
# print(heapq.heappop(h))
# print(heapq.heappop(h))
# print(h)
# print(heapq.heappop(h))


# l = [3, 6, 5, 7, 4, 2, 8]
# heapq.heapify(h1)
# print(heapq.nlargest(3,h1))
# print(heapq.nsmallest(3,h1))

# l = [3, 6, 5, 7, 4, 2, 8]
# h1 = []
# k = 4
# c = 0

# for i in range(len(l)):

#     if c < k :
#         heapq.heappush(h1,l[i])
#         c = c+1
#     else:
#         root = heapq.heappop(h1)

#         if root < l[i]:
#             heapq.heappush(h1, l[i])
        
#         else:
#             heapq.heappush(h1, root)

# print(heapq.heappop(h1))

# Max heap 

# l = [3, 6, 5, 7, 4, 2, 8]
# heapq._heapify_max(l)
# # print(l)

# heapq._heappop_max(l)
# print(l)

# heapq.heappush(l,8)
# print(l)
# heapq._heapify_max(l)
# print(l)

# Heapify 
def heapify(l, root) :
    n = len(l)
    m = root
    left_child = 2*root + 1
    right_child = 2*root + 2

    if left_child < n and l[left_child] < l[m] :
        m = left_child
    
    if right_child < n and l[right_child] < l[m] :
        m = right_child
    
    if m != root :

        l[root],l[m] = l[m],l[root]

        heapify(l,m)
        
# Build heap
# l = [3, 6, 5, 7, 4, 2, 8]
# for i in range(len(l)//2 - 1, -1, -1):
#     heapify(l,i)

# print(l)
