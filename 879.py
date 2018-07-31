from pprint import pprint as print
class Solution:
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        group, profit = zip(*sorted(zip(group, profit), reverse=True))
        self.res = 0
        # print(group, profit)

        def deeper(G, P, group, profit):
            print(G,P,group,profit)
            if len(group) == 0:
                if P <= 0:
                    # print("\t"*t+"OK")
                    self.res += 1
                return

            # accelerate
            if P <= 0 and sum(group) < G:
                # print("early stopping")
                self.res += 2 ** len(group)
                return

            if G >= group[0]:
                deeper(G-group[0], P-profit[0],
                    group[1:],
                    profit[1:])
            deeper(G, P,
                    group[1:],
                    profit[1:])
        deeper(G, P, group, profit)
        return self.res % 1000000007

    def profitableSchemes(self, G, P, group, profit):
        dp = [[0] * (G + 1) for i in range(P + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(P, -1, -1):
                for j in range(G, g-1, -1):
                    dp[min(i + p, P)][j] += dp[i][j-g]
            print(dp)
            print('\n')
        return sum(dp[P]) % (10**9 + 7)


G=10
P=1
group=[8,8,7,4,3,1,1,6,11,3,1,7,6,9,9,1,8,9,3,10,10,8,7,6,9,10,6,2,2,6,9,7,5,6,2,1,2,10,11,6,8,9,9,8,11,6,2,2,4,5,1,2,1,11,3,2,11,7,11,4,5,7,6,9,6,7,10,10,9,10,10,8,8,6,9,8,5,1,2,5,10,1,4,2,1,5,1,3,6,6,10,6,2,3,2,1,9,6,6,4]
profit=[23,36,94,35,73,7,65,25,22,4,62,62,12,18,89,62,2,66,85,94,73,31,56,95,71,91,53,75,100,47,68,4,64,52,97,8,52,32,98,64,2,64,33,21,52,44,41,50,59,40,48,47,39,9,100,1,43,94,63,23,21,92,36,69,100,8,75,16,79,98,72,83,70,11,3,41,91,18,17,76,71,58,71,62,34,49,58,59,90,84,12,43,27,60,47,89,31,14,11,15]
# group = [1,2,3,4]
# profit = [2,3,1,4]

G=10
P=5
group=[2,3,5]
profit=[6,7,8]

# G=10
# P=1
# group=[7,1,9,1,9]
# profit=[1,2,2,1,0]
print(Solution().profitableSchemes(G, P, group, profit))