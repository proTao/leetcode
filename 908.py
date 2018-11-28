class Solution(object):
    def smallestRangeI(self, A, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        upper_bound = [i+k for i in A]
        lower_bound = [i-k for i in A]
        # print(upper_bound)
        # print(lower_bound)
        return max(max(lower_bound) - min(upper_bound), 0)

        


a = [1,3,6]
k = 1
print(Solution().smallestRangeI(a, k))