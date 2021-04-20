"""
Given a string s consisting only of characters a, b and c. 
Return the number of substrings containing at least one occurrence of all these characters a, b and c.

First, not very efficient (time limit exceeded)
"""
def numberOfSubstrings(self, s):
    chars = set(['a', 'b', 'c'])
    result = 0
    i, j = 0, 2
    while i <= len(s)-2 and j <= len(s):
        if j == len(s):
            i += 1
            j = i + 2
        if set(s[i:j+1]) == chars:
            # print(s[i:j+1])
            result += 1
        j += 1
            
                
    return result

""" Now, a more efficient solution (uses a sliding window approach):
"""
def numberOfSubstrings(self, s):
    result = 0
    count = {char: 0 for char in 'abc'}     # keep track of char count within a substring[j:i]
    i = 0
    for j in range(len(s)):
        count[s[j]] += 1
        while all(count.values()):
            count[s[i]] -= 1
            i += 1
        # print(f'{count}, {i}')
        result += i

    return result