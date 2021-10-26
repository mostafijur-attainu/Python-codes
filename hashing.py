# Frequency of each element of an array

arr = [5, 9, 5, 4, 9, 6, 6] # 5 : 2 | 9 : 2 | 4 : 1 | 6 : 2
# Brute force
# for i in range(len(arr)):
#     count = 1

#     if arr[i] != -1 :
#         for j in range(i+1, len(arr)):
#             if arr[i] == arr[j]:
#                 count += 1
#                 arr[j] = -1
    
#         print(arr[i], count)

#Hashing
d = {}

for i in range(len(arr)):

    if arr[i] in d.keys():
        d[arr[i]] += 1
    else:
        d[arr[i]] = 1

print(d)