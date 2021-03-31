def check_next(grid, cur_row, cur_col, cur_word, cur_path):
    R = len(grid)
    C = len(grid[0])
    moves = [[1, 0], [0, 1]]
    if not cur_word:
        return True

    for r,c in moves:
        if cur_row+r < R and cur_col+c < C and grid[cur_row+r][cur_col+c] == cur_word[0]:
            cur_path.append([cur_row+r, cur_col+c])
            if check_next(grid, cur_row+r, cur_col+c, cur_word[1:], cur_path):
                return True

    return False


def findWord(word, grid):
  R = len(grid)
  C = len(grid[0])
      
  result = []
  for r in range(R):
    for c in range(C):
      if grid[r][c] == word[0]:
        result.append([r,c])
        if check_next(grid, r, c, word[1:], result):
          print(result)
          return
  print('None')




grid = [['t', 'c', 'a'], ['r', 'a', 'q'], ['x', 't', 't']]
findWord('cat', grid)
