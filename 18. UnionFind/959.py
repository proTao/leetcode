from typing import List

from unionfind import UnionFind

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        uf = UnionFind(N**2*2+N*2)
        for i in range(N-1):
            for j in range(N-1):
                index = i*N+j
                self.unionSquare(uf, left=index,
                                     right=index+1,
                                     up=index+N**2,
                                     down=index+N**2+N,
                                     marker=grid[i][j])
        for i in range(N-1):
            index=i*N+N-1
            self.unionSquare(uf, left=index,
                                right=N**2*2+i,
                                up=index+N**2,
                                down=index+N**2+N,
                                marker=grid[i][N-1])

        for i in range(N-1):
            index=N*N-N+i
            self.unionSquare(uf, left=index,
                                right=index+1,
                                up=index+N**2,
                                down=N**2*2+N+i,
                                marker=grid[N-1][i])
        self.unionSquare(uf, left=N*N-1,
                            right=N**2*2+N-1,
                            up=N*N+N**2-1,
                            down=N**2*2+N+N-1,
                            marker=grid[N-1][N-1])
        return uf.components
    
    def unionSquare(self, uf, up, left, right, down, marker):
        if marker == '\\':
            # print("\\")
            uf.union(up, right)
            uf.union(left, down)
        elif marker == '/':
            print("/")
            uf.union(up, left)
            uf.union(right, down)
        elif marker == ' ':
            print("-")
            uf.union(up, left)
            uf.union(left, down)
            uf.union(right, down)
        else:
            assert False


    
if __name__ == "__main__":
    grid = [" /","  "]
    print(Solution().regionsBySlashes(grid))