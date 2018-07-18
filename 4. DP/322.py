class Solution:
    def coinChange(self, coins, amount, method="DP"):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # bound
        if len(coins) == 1:
            return amount // coins[0] if amount % coins[0] == 0 else -1

        if method == "BT":
            import sys 
            sys.setrecursionlimit(10000)
            self.res = float("inf")
            def deeper(availible_coins, target, count):
                # print(availible_coins, target, count)
                if target == 0:
                    if count < self.res:
                        print("got it!", count)
                        self.res = count
                if len(availible_coins) == 0:
                    return
                if availible_coins[0] > target:
                    return deeper(availible_coins[1:], target, count)
                deeper(availible_coins, target - availible_coins[0], count+1)
                deeper(availible_coins[1:], target, count)

            deeper(sorted(coins, reverse=True), amount, 0)
            return self.res if self.res < float('inf') else -1

        if method == "DP":
            dp = [0] + [float("inf")] * amount

            for n in coins:
                for i in range(n, amount+1):
                    dp[i] = min(dp[i-n] + 1, dp[i])
                # print(dp)
            return dp[-1] if dp[-1] < float('inf') else -1

a=[186,419,83,408]
b=6249
print(Solution().coinChange(a, b, method="DP"))