class Solution(object):
    # def findMaxAverage(self, nums, k):
    #     """
    #	  我的代码超时了
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: float
    #     """
    #     max_sum = sum(nums[0:k])
    #     for i in range(len(nums)-k+1):
    #         temp = sum(nums[i:i+k])
    #         if max_sum < temp:
    #             max_sum = temp
    #     return (max_sum + 0.0) / k
    def findMaxAverage(self, A, K):
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        ma = max(P[i+K] - P[i] 
                 for i in xrange(len(A) - K + 1))
        return ma / float(K)
