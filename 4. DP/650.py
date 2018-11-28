class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """

        # len=0, 1, 2, 3
        dp = [0,0,2,3] + [0] * (n-3)
        if n <= 3:
            return dp[n]

        for i in range(4, n+1):
            curr = i
            for r in range(2, int(i**0.5//1)+1):
                if i % r == 0:
                    temp = min(dp[r]+int(i/r), dp[int(i/r)]+r)
                    curr = temp if temp < curr else curr
            dp[i] = curr
        
        print([i for i in enumerate(dp)])
        return dp[-1]
print(Solution().minSteps(24))


""" solution
A : None

2A : CV

3A  : CVV

4A  : 2*2 -> CV + CV
    : 1*4 -> CVVV
5A  : 1*5 -> CVVVV

6A  : 2*3 -> CV + CVV
    : 3*2 -> CVV + CV
    : 1*6 -> CVVVVV

7A  : 1*7 -> CVVVVVV

8A  : 1*8 -> CVVVVVVV
    : 2*4 -> CV + CVVV
    : 4*2 -> CVCV + CV

12A : 1*12 -> 12
    : 3*4 -> 3 + 4
    : 4*3 -> 4 + 3
    : 2*6 -> 2 + 6
    : 6*2 -> 5 + 2

14A : 1*14 -> 14
    : 2*7 -> 2 + 7
    : 7*2 -> 7 + 2

24A : 1*24 -> 24
    : 2*12 -> 2 + 12
    : 3*8 -> 3 + 8
    : 4*6 -> 4 + 6
    : 6*4 -> 5 + 4
    : 8*3 -> 6 + 3
    : 12*2 -> 7 + 2

42A : 1*42 -> 42
    : 3*14 -> 3 + 14
    : 14*3 -> 9 + 3
    : 6*7 -> 5 + 7
    : 7*6 -> 7 + 6

递归的思路已经出来了，接下来就是效率的问题。
首先，只要能分解，肯定比不分解好，只要能拆成两个数大于1的因子，那么这两个因子的和肯定小于原来的数。（易证）
再有，如果能拆成两个因子a和b，而且a大于b，那么拆成<a,b>一定比<b,a>好，因为后面的数是重复，重复的话一定是C加上一串V，但是前面的数已经是解决过的最优子问题了，很有可能小，但是怎么着也不会更差。然后仔细一想，不对！大的数不一定最优子问题就比小的数的最优子问题更好，比如大的数是质数，就像42拆分成6和7。

但是我这种方法的效率很低，是n^2的效率，这道题实际上可以转化为贪心，Solution中时间最短那那个提交就是。
他的方法实际上基于一个观察，这道题等价为将一个纸带不停的折叠，但是每次折叠的长度必须是整数，因此实际上就是做因式分解，，将所有质数相加即可。
"""
class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        primeFactors=[]
        for i in range(2,int(n**.5)+1):
            print(i , end=" ")
            while n%i==0:
                primeFactors.append(i)
                n=n//i
                print(n, end=" ")
            print()
        if n>1:
            primeFactors.append(n)
        print(primeFactors)
        return sum(primeFactors)
print("\nbetter solution")
a = Solution()
a.minSteps(120)
