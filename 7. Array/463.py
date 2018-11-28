class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        if height:
            width = len(grid[0])

        res = 0
        count = 0
        # print(height, width)
        for i in range(height):
            for j in range(width):
                gain = self.countEdgeGain(grid, i,j,height,width)
                res += gain
        
        return res

    def countEdgeGain(self, grid, i, j, height, width):
        zero = 0
        one = 0
        if grid[i][j] == 0:
            return 0

        if i == 0:
            zero += 1
        else:
            if grid[i-1][j] == 0:
                zero += 1
            else:
                one +=1
        # print(zero,one)

        if i == height-1:
            zero += 1
        else:
            if grid[i+1][j] == 0:
                zero += 1
            else:
                one +=1
        # print(zero,one)

        if j == 0:
            zero += 1
        else:
            if grid[i][j-1] == 0:
                zero += 1
            else:
                one +=1
        # print(zero,one)

        if j == width-1:
            zero += 1
        else:
            if grid[i][j+1] == 0:
                zero += 1
            else:
                one += 1
        # print(zero, one)

        return zero
        

grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

s = Solution()
res = s.islandPerimeter(grid)
print(res)
