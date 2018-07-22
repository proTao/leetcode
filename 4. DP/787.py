inf = float("inf")

class mydict():
    def __init__(self, flights):
        self.d = dict()
        for i in flights:
            self.d[(i[0], i[1])] = i[2]
        print(self.d)

    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            return inf


    

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # bound
        distance = mydict(flights)
        if K == 0:
            return distance[(src, dst)] if distance[(src, dst)] != inf else -1

        # initial
        dp = [inf] * n
        for i in range(n):
            dp[i] = distance[(src, i)]
            min_dist = min(dp)
        dp[src] = 0

        newdp = [0] * n
        changed = True
        for k in range(K):
            changed = False
            for i in filter(lambda x:x!=src, range(n)):
                if dp[i] != min_dist:
                    relax = min(dp[j]+distance[(j, i)] for j in\
                                filter(lambda x:x != src or x != i, range(n)))
                    print(k,i,relax)
                    if relax < dp[i]:
                        newdp[i] = relax
                        changed = True
                        if relax < min_dist:
                            min_dist = relax
                    else:
                        newdp[i] = dp[i]
                else:
                    newdp[i] = dp[i]
            if changed == False:
                print("early stopping")
                break
            dp = newdp.copy()
            print(dp)
        return dp[dst] if dp[dst] != inf else -1

n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(Solution().findCheapestPrice(n, edges, src, dst, 2))