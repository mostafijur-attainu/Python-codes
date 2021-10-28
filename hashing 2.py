
# Longest substring with no characters repeated
    
def longestSubstring(s):

    i = 0
    n = len(s)
    max_length = 0
    dic = {}
    j = 0
    while i < n and j < n:

        # ans_subs = ""
        while j < n:

            if s[j] not in dic.keys():
                dic[s[j]] = 1
                j = j+1
            else:
                if max_length < j-i:
                    max_length = j-i 

                while s[i] != s[j]:
                    dic.pop(s[i])
                    i = i+1
                
                dic.pop(s[i])
                i = i+1
                break
            
        if j == n:
            if max_length < j-i:
                max_length = j-i
            break
    print(dic)
    return max_length

print(longestSubstring("university"))