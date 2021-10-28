
# Linear search

# A = list(map(int, input().split()))

# e = int(input())
# count = 0
# b = 0
# for i in range(len(A)):

#     if(A[i] == e):
#         print(i)
#         b = 1
#         break

# if b == 0:
#     print("Not present")

# Counting frequency of element 

# for i in range(len(A)):
#     if A[i] == e:
#         count += 1
# print(count)

#Binary search
# A = list(map(int, input().split()))

# e = int(input())

# st = 0
# en = len(A) - 1
# f = 0

# while st <= en :

#     mid = (st + en)//2

#     if A[mid] == e :
#         print(mid)
#         f = 1
#         break
    
#     if(A[mid] < e):
#         st = mid + 1
    
#     else:
#         en = mid - 1

# if f == 0:
#     print("Not found")

# First occurrence of a number k in a sorted array
# def firstPos(arr, st, en, k):

#     firstP = -1
#     while st <= en:
#         mid = (st+en)//2

#         if arr[mid]==k:
#             firstP = mid
#             en = mid - 1
        
#         elif arr[mid] > k:
#             en = mid-1
        
#         else:
#             st = mid+1
#     return firstP


# arr = [ 1,2,2,2,2,2,3,4,6]
# print(firstPos(arr,0,len(arr)-1,5))
