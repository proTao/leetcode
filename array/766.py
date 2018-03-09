class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        r = len(matrix)
        if r == 0:
            return True
        else:
            c = len(matrix[0])
        print("r",r,"c",c)
        if c >= r:
            # upper
            for i in range(1, c):
                for j in range(r-1-max(0,r-c+i)):
                    if matrix[j][i+j] != matrix[j+1][i+j+1]:
                        return False
            # lower
            for i in range(1,r):
                for j in range(r-i-1):
                    if matrix[i+j][j] != matrix[i+j+1][j+1]:
                        return False
        if c < r:
            # lower
            for i in range(1, r):
                for j in range(c-1-max(0,c-r+i)):
                    if matrix[i+j][j] != matrix[i+j+1][j+1]:
                        return False
            # upper
            for i in range(1,c):
                for j in range(c-i-1):
                    if matrix[j][i+j] != matrix[j+1][i+j+1]:
                        return False


        for i in range(min(c,r)-1):
            if matrix[i][i] != matrix[i+1][i+1]:
                return False


        return True

matrix = [[20,45,14,13,6,4],[48,20,45,14,13,6],[22,48,20,45,14,13],[46,22,48,20,45,14],[82,46,22,48,20,45],[39,0,46,22,48,20]]
for i in matrix:
    print(i)

s = Solution()
res = s.isToeplitzMatrix(matrix)
print(res)

