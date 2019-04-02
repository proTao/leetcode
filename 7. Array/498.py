class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        d = 0 # direction flag
        position_i = position_j = 0
        m, n = len(matrix), len(matrix[0])
        res = [0] * (m*n)
        index = 0

        while position_i!=m and position_j!=n:
            res[index] = matrix[position_i][position_j]
            index += 1
            if d == 0: # right-up now
                if position_j == n-1: # touch right bound
                    d = 1
                    position_i += 1
                elif position_i == 0: # touch up bound
                    d = 1
                    position_j += 1
                else:
                    position_i -= 1
                    position_j += 1
            else: # left-down now
                if position_i == m-1: # touch low bound
                    d = 0
                    position_j += 1
                elif position_j == 0: # touch left bound
                    d = 0
                    position_i += 1
                else:
                    position_i += 1
                    position_j -= 1
        return res

if __name__ == "__main__":
    a = [[1,2,3]]
    print(Solution().findDiagonalOrder(a))