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
