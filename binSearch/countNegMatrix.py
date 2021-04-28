class Solution:
    def __init__(self):
        self.result = 0
    def binary_search(self, row):
        left, right = 0, len(row)-1
        if row[left] < 0:
            self.result += len(row)
            return
        if row[right] > 0:
            return
        while left <= right:
            mid = (left + right) // 2
            if row[mid] < 0:
                self.result += (right - mid + 1)
                right = mid-1
            elif row[left] < 0:
                self.result += (mid - left + 1)
            elif row[mid] >= 0:
                left = mid + 1
        return
    
    
    
    def countNegatives(self, grid) -> int:
        # row by row
        for r in grid:
            self.binary_search(r)
            
        return self.result


solve = Solution()
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(f'Negative numbers in grid: {solve.countNegatives(grid)}')
# output: 8