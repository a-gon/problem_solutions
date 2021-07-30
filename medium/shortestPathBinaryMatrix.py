from collections import deque

def shortestPathBinaryMatrix(grid) -> int:
    if not grid or not (grid[0][0] == 0 and grid[-1][-1] == 0):
        return -1
    grid[0][0] = 1
    queue = deque([(0, 0)])
    directions = [(0, 1), (1, 0), (1, -1), (1, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
    while queue:
        r, c = queue.popleft()
        if (r, c) == (len(grid) - 1, len(grid[0]) - 1):   # if reached the end
            return grid[r][c]
        for i, j in directions:
            new_r, new_c = r + i, c + j
            if not (0 <= new_r < len(grid) and 0 <= new_c < len(grid[0])) or grid[new_r][new_c] != 0:
                continue
            grid[new_r][new_c] = grid[r][c] + 1     # increment cur_path_length
            queue.append((new_r, new_c))
    
    return -1