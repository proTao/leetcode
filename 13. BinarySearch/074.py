class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        length = m * n

        Array = lambda index: matrix[index//n][index%n]
        lower = 0
        upper = length
        while lower < upper:
            mid = (lower + upper) // 2
            if Array(mid) == target:
                return True
            elif Array(mid) > target:
                upper = mid
            else:
                lower = mid + 1
        return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
# target = 13
# matrix = [[1,1]]
# ttargett = 0
print(Solution().searchMatrix(matrix, target))