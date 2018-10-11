class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0:
            return []
        res = [-1] * len(nums1)
        min_stack = [nums2[0]]
        dic = {}
        for val in nums2[1:]:
            if not min_stack:
                min_stack.append(val)
            elif val < min_stack[-1]:
                min_stack.append(val)
            else:
                while min_stack and min_stack[-1] < val:
                    dic[min_stack.pop()] = val
                min_stack.append(val)
        for i, val in enumerate(nums1):
            if val in dic:
                res[i] = dic[val]
        print(dic)
        return res


        


nums1 = [4,1,2]
nums2 = [1,3,4,2]
nums1 = [2,4]
nums2 = [1,2,3,4]
# nums1 = [1,2,3,4]
# nums2 = [3,2,1,4]
print(Solution().nextGreaterElement(nums1, nums2))