class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return list(filter(self.judge, range(left, right+1)))

    
    def judge(self, n):
        nums = set(int(i) for i in str(n))
        if 0 in nums:
            return False
        for i in nums:
            if n % i != 0:
                return False
        return True

print(Solution().selfDividingNumbers(1,22))