class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = [0]
        length = len(A)
        for i in range(1, length):
            if A[i-1] < A[i]:
                left.append(left[-1]+1)
            else:
                left.append(0)
        right = [0]*length
        length = len(A)
        for i in range(length-2, -1, -1):
            if A[i+1] < A[i]:
                right[i] = right[i+1]+1
        # print(left, right)
        try:
            res = max(i + j + 1 for i,j in zip(left, right) if i+j+1>=3 and i > 0 and j > 0)
        except:
            res = 0
        return res

a = [2,1,4,7,3,2,5,2,3]
a = [2,2,2]
a = [1,2,3,4,5,6,7,8,9]
print(Solution().longestMountain(a))
        