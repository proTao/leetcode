class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        self.target = target
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, len(matrix[0])-1
        while True:
            i, flag = self._findBiggerInColumn(matrix, j, i, m)
            if flag: return True
            if i >= m: return False

            j, flag = self._findSmallerInRow(matrix, i, 0, j+1)
            if flag: return True
            if j < 0: return False


    def _findBiggerInColumn(self, matrix, c, lower, upper):
        # range: [lower, upper)
        target = self.target
        while lower < upper:
            mid = (lower + upper) >> 1
            if matrix[mid][c] == target:
                return mid, True
            elif matrix[mid][c] < target:
                lower = mid + 1
            else:
                if upper == mid + 1:
                    break
                else:
                    upper = mid + 1

        for i in range(lower, upper):
            if matrix[i][c] == target:
                return i, True
            if matrix[i][c] > target:
                return i, False

        return len(matrix), False

    def _findSmallerInRow(self, matrix, r, lower, upper):
        # range: [lower, upper)
        target = self.target
        while lower < upper:
            mid = (lower + upper) >> 1
            if matrix[r][mid] == target:
                return mid, True
            elif matrix[r][mid] < target:
                if lower == mid:
                    break
                else:
                    lower = mid
            else:
                upper = mid

        for i in range(upper-1, lower-1, -1):
            if matrix[r][i] == target:
                return i, True
            if matrix[r][i] < target:
                return i, False

        return -1, False



matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
matrix =[[1,1]]
k = 1

matrix = [[5],[6]]
k = 5
print(Solution().searchMatrix(matrix, k))