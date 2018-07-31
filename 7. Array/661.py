class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """


        row = len(M)
        column = len(M[0])

        if row == 1 and column == 1:
            return M


        if row == 1:
            result = [[ 0  for i in range(column)]]
            for i in range(1,column-1):
                result[0][i] = (M[0][i-1] + M[0][i] + M[0][i+1])/3
            result[0][0] = (M[0][0] + M[0][1])/2
            result[0][-1] = (M[0][-1] + M[0][-2])/2
            return result

        elif column == 1:
            result = [ [0]  for i in range(row)]
            for i in range(1,row-1):
                result[i][0] = (M[i-1][0] + M[i][0] + M[i+1][0])/3
            result[0][0] = (M[0][0] + M[1][0])/2
            result[-1][0] = (M[-1][0] + M[-2][0])/2
            return result

        else:
            result = [[0 for i in range(column)] for i in range(row)]

            for i in range(1, row-1):
                for j in range(1, column-1):
                    result[i][j] = (M[i-1][j-1] + M[i-1][j] + M[i-1][j+1] +
                                    M[i][j-1] + M[i][j] + M[i][j+1] +
                                    M[i+1][j-1] + M[i+1][j] + M[i+1][j+1]) / 9

            for i in range(1, row-1):
                result[i][0] = (M[i-1][0]+M[i][0]+M[i+1][0]+M[i-1][1]+M[i][1]+M[i+1][1])/6
                result[i][-1] = (M[i-1][-1]+M[i][-1]+M[i+1][-1]+M[i-1][-2]+M[i][-2]+M[i+1][-2])/6

            for i in range(1, column-1):
                result[0][i] = (M[0][i-1] + M[0][i] + M[0][i+1] + M[1][i-1] + M[1][i] + M[1][i+1])/6
                result[-1][i] = (M[-1][i-1] + M[-1][i] + M[-1][i+1] + M[-2][i-1] + M[-2][i] + M[-2][i+1])/6


            result[0][0] = (M[0][0] + M[0][1] + M[1][0] + M[1][1]) /4
            result[0][-1] = (M[0][-1] + M[0][-2] + M[1][-1] + M[1][-2]) /4
            result[-1][0] = (M[-1][0] + M[-1][1] + M[-2][0] + M[-2][1]) /4
            result[-1][-1] = (M[-1][-1] + M[-1][-2] + M[-2][-1] + M[-2][-2]) /4

            return result

s=Solution()

# print(s.imageSmoother([[1,2,3], [1,2,1], [4,4,4]]))
print(s.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))
# print(s.imageSmoother([[2,3]]))