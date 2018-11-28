from unionfind import UnionFind



class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        length =len(M)
        uf = UnionFind(length)
        for i in range(length):
            for j in range(i):
                if M[i][j] == 1:
                    uf.add(i,j)

        return uf.componentsNum()

M = [[1,1,0],
 [1,1,1],
 [0,1,1]]
print(Solution().findCircleNum(M))