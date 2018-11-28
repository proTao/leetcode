class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        items = sorted(nums, reverse=True)
        total = sum(items)
        available = [True] * len(items)
        target = total // k
        print(total, target)
        if target * k != total:
            return False

        for i in range(k):
            sub = self.bagSolution(items, target, available)
            if sub is None:
                return False
            print([items[j] for j in sub])

            for j in sub:
                available[j] = False
        return True

    def bagSolution(self, items, target, available):
        # no input parameter will be changed in this function
        dp = [None for i in range(target+1)]
        dp[0] = list()

        for i, (item, flag) in filter(lambda x: x[1][1], enumerate(zip(items, available))):
            # early stop
            # print(item)
            if dp[-1]:
                return dp[-1]
            for j in range(target, item-1, -1):
                if dp[j]:
                    continue
                if dp[j-item] is not None:
                    dp[j] = dp[j-item] + [i]
        return dp[-1]


a=[11,3,1,11,3,1,13,2,3]
b=3
print(Solution().canPartitionKSubsets(a, b))


