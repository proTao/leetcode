from IndexHeap import IndexMinHeap
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        
        res = max(self.dijkstra(times, N, K))
        if res == float("inf"):
            return -1
        else:
            return res

    def dijkstra(self, times, N, K):
        cost = defaultdict(list)
        for i in times:
            if i[0] in cost:
                cost[i[0]].append((i[1], i[2]))
            else:
                cost[i[0]] = [(i[1], i[2])]
        print(cost)

        self.backtrack = [None] * (N+1)
        self.from_k_to_ = [float("inf")] * (N+1)
        self.from_k_to_[0] = 0 #  这个点没用，下标从1开始
        self.from_k_to_[K] = 0
        self.pq = IndexMinHeap()
        for t, c in cost[K]:
            self.pq.insert(t, c)
        self.pq.insert(K, 0)
        
        while self.pq.size():
            greedy_choose = self.pq.delMin()
            self.relaxVertax(greedy_choose, cost[greedy_choose])

        print(self.backtrack)
        print(self.from_k_to_)
        return self.from_k_to_
        


    def relaxEdge(self, edge_s, edge_t, d):
        if self.from_k_to_[edge_s] + d < self.from_k_to_[edge_t]:
            self.from_k_to_[edge_t] = self.from_k_to_[edge_s] + d
            self.backtrack[edge_t] = edge_s
            if not self.pq.contains(edge_t):
                self.pq.insert(edge_t, self.from_k_to_[edge_t])
            elif self.from_k_to_[edge_t] < self.pq.keyOf(edge_t):
                self.pq.change(edge_t, self.from_k_to_[edge_t])
            else:
                pass


    def relaxVertax(self, edge_s, edge_list):
        for t, cost in edge_list:
            self.relaxEdge(edge_s, t, cost)


times = [(0,1,6),(0,2,3),(2,1,2),(1,2,2),(1,3,5),(2,3,3),(2,4,4),(3,4,2),(4,3,2),(3,5,3),(4,5,5)]
N=6
K=0

times=[[2,1,1],[2,3,1],[3,4,1]]
N=4
K=2

print(Solution().networkDelayTime(times, N, K))