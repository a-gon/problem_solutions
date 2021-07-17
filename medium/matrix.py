# Determine if matrix is a square matrix
# Print horizontal zigzag of matrix
# • Rotate matrix 90 degrees clockwise
# • Spiral matrix backwards
# • Matrix outer sum
# Set zeros in matrix

def isSquare(m):
    rows = len(m)
    cols = len(m[0])
    return rows == cols

print(isSquare([[1,1], [2,3]]))

def printZigZag(m):
    result = []
    reversed_order = False
    for r in range(len(m)):
        if reversed_order:
            result.extend(reversed(m[r]))
        else:
            result.extend(m[r])
        
        reversed_order = not reversed_order
    
    return result

m = [[1,2,3], [4,5,6], [7,8,9]]
print(printZigZag(m))

def spiralOrder(self, matrix):
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    result = []
    while left <= right and top <= bottom:
        result += [matrix[top][col] for col in range(left, right)]
        top += 1
        result += [matrix[row][right - 1] for row in range(top, bottom)]
        right -= 1
        if top >= bottom:
            break
        result += [matrix[bottom - 1][col] for col in reversed(range(left, right))]
        bottom -= 1
        if left >= right:
            break
        result += [matrix[row][left] for row in reversed(range(top, bottom))]
        left += 1
        
    return result