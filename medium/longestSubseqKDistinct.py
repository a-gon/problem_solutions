def longestSubsequenceKDistinct(s, k):
    '''
    Given a string s, return the length of the longest substring that contains at most k distinct characters.
    '''
    if len(s) < k:
        return len(s)
    window = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        char = s[right]
        window[char] = right
        if len(window) > k:
            # remove leftmost char from cur window, exclude it from the slidig window
            leftmost_ind_del = min(window.values())
            del window[s[leftmost_ind_del]]
            left = leftmost_ind_del + 1
        
        max_len = max(max_len, right - left + 1)   # no +1 if using while loop instead of for
    
    return max_len

print(longestSubsequenceKDistinct('ccaabbb', 2), 'expected 5')
print(longestSubsequenceKDistinct('ccaabbb', 3), 'expected 7')
print(longestSubsequenceKDistinct('ecebakgnab', 5), 'expected 7')
