class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # best answer
        # return list(set(nums1) & set(nums2))

        a = sorted(list(set(nums1)))
        b = sorted(list(set(nums2)))
        print(a,b)
        res = []
        i = j = 0
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

nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersection(nums1, nums2))
        