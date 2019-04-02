from typing import List
from collections import deque

def genNeighbor(i, j, m, n):
    if i>0:
        yield i-1, j
    if j>0:
        yield i, j-1
    if i<m-1:
        yield i+1, j
    if j<n-1:
        yield i, j+1

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        queue = deque()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i,j))
                else:
                    matrix[i][j] = -1
        print(matrix)
        step = 1
        while queue:
            length = len(queue)
            for _ in range(length):
                i, j = queue.popleft()
                for next_i, next_j in genNeighbor(i,j,m,n):
                    if matrix[next_i][next_j] < 0:
                        matrix[next_i][next_j] = step
                        queue.append((next_i, next_j))
            step += 1
        return matrix

if __name__ == "__main__":
    a = [[0,0,0],[0,1,0],[1,1,1]]
    print(Solution().updateMatrix(a))