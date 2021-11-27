# Dynamic programming

listFib = [0]*10

# def fib(n):
#     global listFib

#     if n == 1 :
#         listFib[n] = 0
#         return 0
    
#     if n == 2 :
#         listFib[n] = 1
#         return 1
    
#     if listFib[n] > 0 :
#         return listFib[n]
 
#     fib1 = fib(n-1) 
#     fib2 = fib(n-2)

#     listFib[n] = fib1 + fib2

#     return listFib[n]

# print(fib(20))
# print(fib(35))
# print(fib(95))

# Staircase problem
# def numOfWays(curr, n):

#     if curr == n:
#         return 1
    
#     if curr > n :
#         return 0
    
#     if numOfWaysList[n] > 0 :
#         return numOfWaysList[n]
    
#     numOfWaysList[n] = numOfWays(curr+1,n) + numOfWays(curr+2,n) + numOfWays(curr + 3, n)

#     return numOfWaysList[n]

# numOfWaysList = [0]*1000

# numOfWaysList[0] = 1
# n = int(input())
# for i in range(1,n+1):

#     if i-1 >= 0:
#         numOfWaysList[i] += numOfWaysList[i-1]

#     if i-2 >= 0:
#         numOfWaysList[i] += numOfWaysList[i-2]

#     if i-3 >= 0:
#         numOfWaysList[i] += numOfWaysList[i-3]

# print(numOfWaysList[n])    

# Longest increasing subsequence
# dp = [1]*5

# arr = [5,9,4,2,6]

# for i in range(1,len(arr)):

#     for j in range(i-1,-1,-1):

#         if arr[j] < arr[i] :

#             dp[i] = max(dp[i], dp[j]+1)

# print(dp)

# print(max(dp))

# Nth power of 2
# power = [0]*11

# power[0] = 1

# for i in range(1,11):

#     power[i] = power[i-1]*2

# print(power[10])
