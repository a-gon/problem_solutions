
def numIslands(grid):
    '''
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.
    '''
    def bfs(grid, start):
        nonlocal num_islands
        neighbors = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        queue = [start]
        while queue:
            cur_r, cur_c = queue.pop(0)

            if grid[cur_r][cur_c] == '-1': # already visited
                continue
            grid[cur_r][cur_c] = '-1'
            for r, c in neighbors:
                if (cur_r + r) < 0 or (cur_r + r) >= len(grid) or cur_c + c < 0 or cur_c + c >= len(grid[0]): # out of bounds
                    continue
                if grid[cur_r + r][cur_c + c] == '1': # only append neighbor if it is land
                    queue.append([cur_r + r, cur_c + c])
                
        num_islands += 1 # finished traversing all adjacent -> end of island
        
#                 visit all neighbors, marking them as -1
#                  increment num of islands when done
    # iterate over the matrix:

    num_islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':       # only if it is land and not visited yet
                bfs(grid, [r, c])
                
    return num_islands