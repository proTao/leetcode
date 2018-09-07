class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = sorted(nums1)
        b = sorted(nums2)
        i = 0
        j = 0
        res = []
        while i<len(a) and j<len(b):
            if a[i] < b[j]:
                i += 1
            elif a[i] > b[j]:
                j += 1
            else: 
                res.append(a[i])
                i += 1
                j += 1
        return res

print(Solution().intersect([1,2,2,1], [2,2,2]))
