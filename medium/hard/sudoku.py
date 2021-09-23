def solveSudoku(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    def isValid(row, col, num):
        for r in range(9):
            if board[r][col] == num:
                return False
        for c in range(9):
            if board[row][c] == num:
                return False
        
        boxRow, boxCol = 3 * (row // 3), 3 * (col // 3)
        for r in range(boxRow, boxRow + 3):
            for c in range(boxCol, boxCol + 3):
                if board[r][c] == num:
                    return False
        return True
    
    def backtrack(row, col):
        while board[row][col] != '.':
            col += 1
            if col == 9:
                col = 0
                row += 1
            if row == 9:
                return True
        
        for num in range(1, 10):
            if isValid(row, col, str(num)):
                board[row][col] = str(num)
                if backtrack(row, col):
                    return True
        
        board[row][col] = '.'
        return False
    
    
    backtrack(0, 0)
    return board

input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

expectedOutput = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]


assert solveSudoku(input) == expectedOutput, 'Invalid solution'