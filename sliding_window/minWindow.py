import collections
def minWindow(s: str, t: str) -> str:
    '''
    Return min window (part of string s) that contains all characters from string t
    '''
    l, r = 0, 0
    chars = {}
    t_counter = collections.Counter(t)
    minWindow = (0, float('inf'))
    while l <= r < len(s):
        chars[s[r]] = chars.get(s[r], 0) + 1

        while all(ch in chars and chars[ch] >= t_counter[ch] for ch in t_counter):
            if r - l < minWindow[1] - minWindow[0]:
                minWindow = (l, r)
            chars[s[l]] -= 1
            l += 1
        
        r += 1
            
    return s[minWindow[0] : minWindow[1] + 1] if minWindow[1] < float('inf') else ''



s = "ADOBECODEBANC"
t = "ABC" 
# "BANC"
print(minWindow(s, t), 'expect BANC')
print(minWindow('a', 'a'), 'expect a')
print(minWindow('a', 'aa'), 'expect ''')


