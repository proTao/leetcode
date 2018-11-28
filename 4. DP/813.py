from copy import copy
from pprint import pprint as print
class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        if K == len(A):
            return sum(A)


        # initial
        # because maybe often culculate average, so pre calculate all the average
        average = [[0] * (len(A)+1) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(i+1, len(A)+1):
                average[i][j] = sum(A[i:j])/(j-i)

        if K == 1:
            return average[0][len(A)]
        
        # tableing:dp[k][j] meaning the best solution of subQ : A[:j] split to k
        dp = copy(average[0][1:])
        print(dp)
        for k in range(1, K-1):
            for j in range(len(A)-1, k-1, -1):
                if j == k:
                    dp[j] = sum(A[:j+1])
                else:
                    dp[j] = max(dp[i]+average[i+1][j+1] for i in range(k-1,j))
            print(dp)


        # return 
        return max(dp[i]+average[i+1][len(A)] for i in range(K-2,len(A)-1))
            

print(Solution().largestSumOfAverages([9,1,2,3,9], 1))