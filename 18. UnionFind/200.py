class UnionFind():
    def __init__(self, length):
        self.length = length
        self.components = length
        self.pre = [i for i in range(length)]

    def root(self, i):
        # find root
        length = 0
        c = i
        while self.pre[i] != i:
            i = self.pre[i]
            length += 1
        root = i

        # path compress
        temp = self.pre[c]
        while temp != c:
            self.pre[c] = root
            c = temp
            temp = self.pre[c]
        return root

    def isConnect(self, i, j):
        return self.root(i) == self.root(j)

    def add(self, i, j):
        print(i,j)
        root_i, root_j = self.root(i), self.root(j)
        if root_i != root_j:
            self.pre[root_i] = root_j
            self.components -= 1
        print(self.components)

    def componentsNum(self):
        return self.components


class Solution:
    def numIslands(self, grid) -> int:
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        if m*n == 1:
            return int(grid[0][0])
        water = None
        uf = UnionFind(m * n)
        for i in range(m-1):
            for j in range(n-1):
                if grid[i][j] == '1':
                    if grid[i][j+1] == '1':
                        uf.add(i*n+j, i*n+j+1)
                    if grid[i+1][j] == '1':
                        uf.add(i*n+j, i*n+n+j)
                else:
                    if water is None:
                        water = i*n+j
                    else:
                        uf.add(i*n+j, water)
                        
        for i in range(n-1):
            if grid[m-1][i] == '1':
                if grid[m-1][i+1] == '1':
                    uf.add(m*n-n+i, m*n-n+i+1)
            else:
                if water is None:
                    water = m*n-n+i
                else:
                    uf.add(m*n-n+i, water)
                    
        for i in range(m-1):
            if grid[i][n-1] == '1':
                if grid[i+1][n-1] == '1':
                    uf.add(i*n+n-1, i*n+n+n-1)
            else:
                if water is None:
                    water = i*n+n-1
                else:
                    uf.add(i*n+n-1, water)

        if grid[m-1][n-1] == '1':
            if grid[m-1][n-2] == '1':
                uf.add(m*n-1, m*n-2)
            if grid[m-2][n-1] == '1':
                uf.add(m*n-1, m*n-1-n)
        else:
            if water is not None:
                uf.add(m*n-1, water)


        if water is not None:
            return uf.componentsNum()-1
        else:
            return 1


if __name__ == "__main__":
    grid = [["0","0","0","0","0","0","0"]]
    
    
    print(Solution().numIslands(grid))