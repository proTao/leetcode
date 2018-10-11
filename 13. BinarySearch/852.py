class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = 0
        r = len(A) - 1
        while True:
            mid = (l + r) // 2
            if A[mid-1] < A[mid] > A[mid+1]:
                break
            elif A[mid-1] < A[mid] < A[mid+1]:
                l = mid
            else:
                r = mid
        # print(A[mid])
        return mid

A = [3,4,5,6,7,6,5,4,3,2,1]
print(Solution().peakIndexInMountainArray(A))