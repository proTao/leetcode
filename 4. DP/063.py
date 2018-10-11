class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
             return 0

        try :
            first_1 = obstacleGrid[0].index(1)
            cache = [1] * first_1 + [0] * (len(obstacleGrid[0])-first_1)
        except ValueError as e:
            cache = [1] * len(obstacleGrid[0])

        print(cache) 
        for i in range(1, len(obstacleGrid)):
            for j in range(len(cache)):
                if obstacleGrid[i][j] == 1 :
                    cache[j] = 0
                elif j > 0:
                    cache[j] = cache[j] + cache[j-1]
                else:
                    pass

            print(cache)
        return cache[-1]

s = Solution()
g=[
      [0],[1]
]
print(s.uniquePathsWithObstacles([[0],[1]]))


