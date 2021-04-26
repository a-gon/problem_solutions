""" Longest common sunsequence - not necessarily contiguos """
def lcs(s1, s2):
    cache = [[0 for j in range(len(s1)+1)] for j in range(len(s2)+1)]
    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1):
            if s1[j-1] == s2[i-1]:

                cache[i][j] = cache[i-1][j-1] + 1
            else:
                cache[i][j] = max(cache[i-1][j], cache[i][j-1])

    return cache[-1][-1]




s1 = 'AGGTAB'
s2 = "GXTXAYB"
print(f'longest common subsequence is {lcs(s1, s2)}')
# Output: 4
