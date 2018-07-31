from heapq import heappop, heappush

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        r = len(matrix)
        c = len(matrix[0])
        heap = [(matrix[0][0],0,0)]
        marked = set()
        while k > 0:
            v, i, j = heappop(heap)
            # print(v,i,j)
            if i + 1 < r and (i+1, j) not in marked:
                heappush(heap, (matrix[i+1][j],i+1,j))
                marked.add((i+1, j))
            if j + 1 < c and (i, j+1) not in marked:
                heappush(heap, (matrix[i][j+1],i,j+1))
                marked.add((i, j+1))
            k -= 1
        return v


matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(Solution().kthSmallest(matrix, k))