# from pprint import pprint as print

directions = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
next_step = lambda p : (tuple(sum(i) for i in zip(d,p)) for d in directions)
feasible_step = lambda N,p: (i for i in next_step(p) if 0<=i[0]<N and 0<=i[1]<N)
feasible_count = lambda N,p: sum(0<=i[0]<N and 0<=i[1]<N for i in next_step(p))


class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        feasible_count_lookup = {(i,j):feasible_count(N, (i,j)) for i in range((N+1)//2) for j in range(i,(N+1)//2)}
        # print(feasible_count_lookup)
        cache = {}
        def mapToLookup(p, N):
            new_x = N-1-p[0] if p[0] >= (N+1)//2 else p[0]
            new_y = N-1-p[1] if p[1] >= (N+1)//2 else p[1]
            return min(new_x, new_y), max(new_x, new_y)

        def nextProb(p,N,K):
            # print(p,N,K)
            if (p,K) in cache:
                return cache[(p,K)]
            print(p,K)
            if K == 1:
                return feasible_count_lookup[mapToLookup(p, N)]/8
            else:
                res = sum(nextProb(nextp, N, K-1)/8 for nextp in feasible_step(N, p))
                cache[(p,K)] = res
                return res

        if K == 0:
            return 1
        return nextProb((r,c),N,K)

class StandardSolution(object):
    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r+dr][c+dc] += val / 8.0
            dp = dp2

        return sum(map(sum, dp))

print(StandardSolution().knightProbability(8,30,6,4))
