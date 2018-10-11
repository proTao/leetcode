class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
            
        def deeper(i, j, grid):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=="1":
                grid[i][j] = "0"

                deeper(i-1, j, grid)
                deeper(i+1, j, grid)
                deeper(i, j-1, grid)
                deeper(i, j+1, grid)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    deeper(i,j, grid)
                    count += 1
        return count


grid = [["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]]

print(Solution().numIslands(grid))