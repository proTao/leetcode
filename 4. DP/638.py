"""
# use numpy
import numpy
class Solution:

    def shoppingOffers(self, prices, special, needs):
        prices = numpy.array(prices)
        needs = numpy.array(needs)

        def deeper(k, needs, i=0):
            if k == 0:
                return numpy.dot(needs, prices)
            if sum(needs) == 0:
                return 0
            temp = needs - special[k-1][:-1]

            temp[temp < 0] = 0

            temp2 = needs - special[k-1][:-1]

            # 如果还不及直接买了
            if numpy.dot(needs - temp, prices) <= special[k-1][-1] or numpy.any(temp2<0):
                return deeper(k-1, needs,i+1)
            else:
                return min(deeper(k-1, needs, i+1), deeper(k, temp, i+1) + special[k-1][-1])

        return int(deeper(len(special), needs))
"""


class Solution:

    def shoppingOffers(self, prices, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        def deeper(k, needs, i=0):
            print("\t"*i, k, needs)
            if k == 0:
                return sum(a*b for a,b in zip(needs, prices))
            if sum(needs) == 0:
                return 0

            use_offer1 = [a-b for a,b in zip(needs, special[k-1][:-1])]
            use_offer2 = [max(a,0) for a in use_offer1]

            # 如果还不及直接买了
            if sum((a-b)*c for a,b,c in zip(needs, use_offer2, prices)) <= special[k-1][-1]\
                    or any(a<0 for a in use_offer1):
                return deeper(k-1, needs,i+1)
            else:
                return min(deeper(k-1, needs, i+1), deeper(k, use_offer2, i+1) + special[k-1][-1])

        return deeper(len(special), needs)

prices = [2,3,4] 
offers = [[1,1,0,4],[2,2,1,9]] # 商品，可以买多个
needs = [1,2,1] # 目标(背包问题中是不能超过这个数，这里是不能低于这个数）

# 感觉和背包问题很像
print(Solution().shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))

# 还有改进余地
# 子问题是花费的最小价格？递推公式
# f(前k个offer，needs=（x，y）) = min（f（前k个offer，needs=max（（needs-offer），零向量））+offer的价格，f（前k-1个offer，needs=needs）

# 边界：k=0时，f=dot(prices, needs)；needs全为零，f=0

class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        def dfs(curr, special, needs):
            p=curr+sum(p*needs[i] for i,p in enumerate(price))
            for si in range(len(special)):
                s = special[si]
                if all(n>=s[i] for i,n in enumerate(needs)):
                    p=min(p, dfs(curr+s[-1], special[si:], [n-s[i] for i,n in enumerate(needs)]))
                # else: p=min(p, dfs(curr, special[si+1:], needs))
            return p
        return dfs(0, special, needs)
