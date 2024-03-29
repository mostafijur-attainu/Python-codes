
# Recursion

# Product of first N natural numbers

# def prod(N):

#     if N == 1:
#         return 1
#     smallRes = prod(N-1)
#     finalRes = smallRes*N

#     return finalRes

# print(prod(6))

# Sum of all array elements using recursion

# def arraySum(A, n):

#     # Base case
#     if n==1:
#         return A[n-1]

#     return arraySum(A,n-1) + A[n-1]

# Reverse string recursively

# def revString(s):

#     if(len(s) == 0):
#         return s

#     smallRes = revString(s[1:])

#     finalRes = smallRes + s[0]

#     return finalRes

# s = input()
# print(revString(s))

# Fibonacci

# def fibonacci(n):

#     # if n<=0:
#     #     return 0
#     if n==1:
#         return 0
#     if n==2:
#         return 1

#     fibx = fibonacci(n-1)
#     fiby = fibonacci(n-2)

#     return fibx + fiby

# n = int(input())
# for i in range(1,n+1):
#     print(fibonacci(i))


# Stair case problem :

# def Nthstair(curr,n):

#     if curr == n:
#         return 1
    
#     if curr > n :
#         return 0
    
#     numofways1 = Nthstair(curr+1, n)
#     numofways2 = Nthstair(curr+2, n)
#     numofways3 = Nthstair(curr+3, n)

#     return numofways1 + numofways2 + numofways3

# n = int(input())
# print(Nthstair(0,n))

# binary search using recursion

# def binarySearch(arr, st, en, k):
    
#     if st>en:
#         return -1

#     mid = (st+en)//2
    
#     if arr[mid] == k :
#         return mid
    
#     if arr[mid] > k:
#         return binarySearch(arr,st,mid-1,k)
    
#     if arr[mid] < k:
#         return binarySearch(arr,mid+1,en,k)

# arr = [1, 5, 6, 7, 8, 9, 10, 15]

# print(binarySearch(arr,0,7,15))
