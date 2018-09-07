class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = m + n - 1
        for n in reversed(nums2):
            while i >= 0 and nums1[i] > n:
                nums1[j] = nums1[i]
                i -= 1
                j -= 1
            nums1[j] = n
            j -= 1

a = [3,0]
b = [1]
la, lb = 1, 1
Solution().merge(a,la,b,lb)
print(a)