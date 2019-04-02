from typing import List

from unionfind import LinkedUnionFind

class Solution:
    def calcEquation(self, equations: List[List[str]], 
                           values: List[float], 
                           queries: List[List[str]]) -> List[float]:
        uf = LinkedUnionFind()
        calc = {}
        for (o1, o2), val in zip(equations, values):
            uf.add(o1)
            uf.add(o2)
            path1 = uf.path(o1)
            path2 = uf.path(o2)
            changed, root_o1, root_o2 = uf.union(o1, o2)
            if changed == o1:
                calc[(root_o1, root_o2)] = (1/self.calcPath(path1, calc))*\
                                            val*\
                                            self.calcPath(path2, calc)
            if changed == o2:
                calc[(root_o2, root_o1)] = (1/self.calcPath(path2, calc))*\
                                            (1/val)*\
                                            self.calcPath(path1, calc)

        ans = [-1] * len(queries)
        for i, (o1, o2) in enumerate(queries):
            if o1 not in uf or o2 not in uf or not uf.isConnect(o1, o2):
                continue
            root = uf.find(o1)
            if o1 == o2:
                ans[i] = 1
            elif root == o1:
                ans[i] = 1/self.calcPath(uf.path(o2), calc)
            elif root == o2:
                ans[i] = self.calcPath(uf.path(o1), calc)
            else:
                ans[i] = self.calcPath(uf.path(o1), calc) / self.calcPath(uf.path(o2), calc)

        return ans

    def calcPath(self, path, calc):
        if len(path) == 1:
            return 1
        if (path[0], path[-1]) in calc:
            return calc[(path[0], path[-1])]
        if (path[-1], path[0]) in calc:
            return calc[(path[-1], path[0])]
        prod = 1
        i = path[0]
        for j in path[1:]:
            prod *= calc[(i,j)]
            i = j
        calc[path[0], path[-1]] = prod
        return prod

if __name__ == "__main__":
    equations = [["a","b"],["e","f"],["b","e"]]
    values = [3.4,1.4,2.3]
    queries = [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]

    print(Solution().calcEquation(equations, values, queries))