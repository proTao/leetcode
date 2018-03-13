from math import ceil
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        # initial
        s = []
        factorial = [1]
        for i in range(1,n+1):
            factorial.append(factorial[-1]*i)
        if k<1 or k>factorial[-1]:
            return ""
        candidates = list(range(1,n+1))

        for i in range(n-1,-1,-1):
            choose = ceil(k / factorial[i])
            s.append(str(candidates[choose-1]))
            candidates.remove(candidates[choose-1])
            k -= (choose-1) * factorial[i]
        return "".join(s)


        

s = Solution()

for i in range(6):
    print(s.getPermutation(3, i+1))
