def Solution():
    min_cost_1 = 0
    min_cost_2 = 0

    def caller():
        pass

    def minCostClimbingStairs(cost):
        n = len(cost)
        # memo = [0 for i in range(n)]
        memo = [_minCost(i, cost[i-1], cost[i-2]) for i in range(n+1)]
        return memo[-1]

    def _minCost(k, cost_1, cost_2):
        if k <= 1:
            return 0
        nonlocal min_cost_1
        nonlocal min_cost_2
        
        res = min(min_cost_1+cost_1, min_cost_2+cost_2)
        min_cost_2 = min_cost_1
        min_cost_1 = res
        return res

    # caller.minCost = minCost
    caller.minCostClimbingStairs = minCostClimbingStairs
    return caller

s = Solution()
cost = [1, 100, 1, 1, 1, 100]
print(s.minCostClimbingStairs(cost))
