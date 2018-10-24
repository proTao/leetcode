from unionfind import UnionFind
from collections import defaultdict
class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        visited = defaultdict(lambda :0)
        father = {}
        uf = UnionFind(len(edges)+1)
        res = None

        double_father_flag = False
        cand = []
        for i,j in edges:
            visited[i] += 1
            visited[j] += 1
            if j in father:
                double_father_flag = True
                cand.append(father[j])
                cand.append(i)
            else:
                father[j] = i
            if not uf.isConnect(i, j):
                uf.add(i, j)
            else:
                res = i,j
        if double_father_flag:
            if visited[cand[0]]
        return res

edges = [[2,1],[3,1],[4,2],[1,4]]
print(Solution().findRedundantDirectedConnection(edges))

        
