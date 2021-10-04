# 1. Product of first N natural numbers : 1*2*3*4*...*N
#  CODE
# n = int(input())

# product = 1

# for i in range(1,n+1,1):
#     product = product*i

# print(product)

# 2. Print first N natural numbers in reverse order : N N-1 N-2 .... 3 2 1

#n = int(input())

# for i in range(n,0,-1):
#     print(i)

# 3. While loop

#EXAMPLE 1

#  n = int(input())

# i = n

# while i > 0:
#     print(i)
#     i = i-1

# EXAMPLE 2
# n = int(input())

# sum = 0
# i = 1

# while i <= n:
#     sum = sum + i
#     i = i + 1

# print(sum)

# Assignment 1 :
#  12345
#  1234
#  123
#  12
#  1

# for i in range(0,5,1) :
     
#     for j in range(0,5-i):
#         print(j+1, end="")
    
#     print()

# Assignment 2 :
# *
# **
# ***
# ****
# *****

# for i in range(5):

#     for j in range(i+1):
#         print("*", end="")
    
#     print()

# Methods

# def printNumbers(n):

#     for i in range(1,n+1,1):
#         print(i, end = " ")
    
#     print()

# printNumbers(5)
# printNumbers(6)
# printNumbers(4)
# printNumbers(7)
