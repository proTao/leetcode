class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            # print(n)
            if(n % 2 == 1):
                count +=1
                # print("aha")
            n = n // 2
        return count

s=Solution()
print(s.hammingWeight(11))