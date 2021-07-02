""" Longest common sunsequence - not necessarily contiguos """
def lcs(s1, s2):
    if not s1 or not s2:
        return []
    dp = [[[] for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            char1 = s1[i - 1]
            char2 = s2[j - 1]
            if char1 == char2:
                dp[i][j] = dp[i - 1][j - 1] + [char1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    return dp[-1][-1]

print(lcs('aba', 'aaz'), 'expected: ["a", "a"]')
print(lcs('abndgrwqa', 'bbbrz'), 'expected: ["b","r"]')




s1 = 'AGGTAB'
s2 = "GXTXAYB"
print(f'longest common subsequence is {lcs(s1, s2)}')
# Output: 4

'''
Longest common sunsequence in two strings
aba, aaz -> 'aa' is the longest common subsequence
lcs('aba', 'aaz')
    max( lcs('ab', 'aaz'),                       lcs('aba, 'aa')) -> 2
      max(lcs('a', 'aaz'), lcs('ab', 'aa'))                 1 + lcs('ab', a) -> 2
max(lcs('', 'aaz'), lcs('a', 'aa'))     max(lcs('a', 'aa'), lcs('ab', a))     max(lcs(a, a), lcs(ab, '')) = 1

1. init dp table of length n+1 by m+1
2. init the table with empty strings
3. calculate lcs for each pair from s1 and s2 
    cases:
    char1 == char2: lcs = max(lcs(s1-char1, s2), lcs(s1, s2-char2))
    char1 != char2: lcs = 1 + lcs(s1-char1, s2-char2)
4. iterate through the 2d table setting each value according to the cases - set or append new char to each cell
5. return the string/set of chars in the rightmost cell

      a b a
   ---------
    / / / /
  a / a a aa
  a / a a aa
  z / a a aa

'''