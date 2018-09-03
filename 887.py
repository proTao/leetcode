class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # initial
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        top = 0
        left = 0
        front = 0

        # calculate
        for line in grid:
            for i in line:
                if i > 0:
                    top += 1
        
        for line in grid:
            front += max(line)
        
        for j in range(len(grid[0])):
            temp_max = 0
            for i in range(len(grid)):
                temp_max = max(grid[i][j], temp_max)
            left += temp_max
        print(top, left, front)
        return top + left + front
                    



grid = [[1,2],[3,4]]
print(Solution().projectionArea(grid))