Longest subarray with all integers same

# Brute force O(N*N*N) - time complexity, O(1) - space complexity

# arr = [1, 2, 2, 2, 5]
# ans = 1
# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         subarr = arr[i:j+1]
#         f = 0
#         for k in range(1,len(subarr)):
#             if subarr[k] != subarr[k-1]:
#                 f = 1
#                 break
        
#         if f == 0:
#             if ans < len(subarr):
#                 ans = len(subarr)


# print(ans)

# Two pointers -- O(N)-- Time complexity, O(N) space complexity
# arr = [1, 2, 2, 3, 2]

# i = 0
# ans = 1

# while i < len(arr):

#     j = i+1

#     while (j < len(arr)) and (arr[j] == arr[j-1]):
#         j += 1
    
#     if ans < j-i:
#         ans = j-i 
    
#     i = j
# print(ans)
