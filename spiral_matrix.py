class Solution:
    def spiralOrder(self, matrix):
        result = []
        up, down = 0, len(matrix)-1
        col1, col2 = 0, len(matrix[0])-1
        
        while up <= down and col1 <= col2:
            # add upper row
            for i in range(col1, col2+1):
                result.append(matrix[up][i])
            # add right col
            for i in range(up+1, down+1):
                result.append(matrix[i][col2])
            # check boundaries
            if up >= down or col1 >= col2:
                break
            # add bottom row
            for i in range(col2-1, col1, -1):
                result.append(matrix[down][i])
            # add left col
            for i in range(down, up, -1):
                result.append(matrix[i][col1])
                
            # update boundaries
            col1 += 1
            col2 -= 1
            up += 1
            down -= 1
            
        
        return result