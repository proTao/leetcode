class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_land = 0
        height = len(grid)
        if height > 0:
            width = len(grid[0])
        else:
            return max_land
        # print(height, width)
        there_is_a_land = -1
        while True:
        # for c in range(2):
            there_is_a_land = self.findLand(grid,there_is_a_land+1,height,width)
            # print("there_is_a_land",there_is_a_land)
            if there_is_a_land < 0:
                break
            else:
                new_land = self.getArea(grid, there_is_a_land//width, 
                    there_is_a_land%width, height, width)
                # print("new_land", new_land)
                if new_land > max_land:
                    max_land = new_land
        return max_land

    # 行扫描方式找下一块陆地
    def findLand(self, grid, last_index, height, width):
        i = last_index
        max_index = height * width
        while(i < max_index):
            if grid[i//width][i%width] == 1:
                return i
            i += 1
        else:
            return -1

    def getArea(self, grid, i, j, height, width):
        # print(i,j)
        if i<0 or j<0 or i>=height or j>=width or grid[i][j]==0:
            return 0
        else:
            grid[i][j] = 0
            return 1 + self.getArea(grid, i-1, j, height, width) +\
                        self.getArea(grid, i+1, j, height, width) +\
                        self.getArea(grid, i, j-1, height, width) +\
                        self.getArea(grid, i, j+1, height, width)


grid = \
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

s = Solution()
res = s.maxAreaOfIsland([[1]])

for i in grid:
    print(i)
print(res)
