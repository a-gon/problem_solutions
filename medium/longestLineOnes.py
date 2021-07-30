def longestLine(mat):
    if not mat:
        return 0
    max_ones = 0

    def dfs(r, c, direction, count):
        nonlocal max_ones
        if not (0 <= r < len(mat) and 0 <= c < len(mat[0])):
            return 
        if mat[r][c] == 1:
            max_ones = max(max_ones, count + 1)
            dfs(r + direction[0], c + direction[1], direction, count + 1)  
            
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == 0:
                continue
            if len(mat) - r > max_ones or len(mat[0]) - c > max_ones: # don't go further if we've already found the longest possible line
                max_ones = max(1, max_ones)
                dfs(r, c, (0, 1), 0) # recursively check to the right
                dfs(r, c, (1, 0), 0) # down
                dfs(r, c, (1, 1), 0) # right diag
                dfs(r, c, (1, -1), 0) # left diag
            
    return max_ones

m1 = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
m2 = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]

print(longestLine(m1), 'expect 3')
print(longestLine(m2), 'expect 4')



