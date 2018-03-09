class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # two pass by hash
        # dic = {}
        # for i in range(len(nums)):
        #     if nums[i] not in dic:
        #         dic.setdefault(nums[i],i)

        # for i in range(len(nums)):
        #     if target-nums[i] in dic:
        #         other_index = dic[target-nums[i]]
        #         if other_index == i:
        #             continue
        #         return (min(i,other_index),max(i,other_index))


        # one pass by hash
        dic={}
        for i in range(len(nums)):
            if target-nums[i] in dic:
                return sorted([dic[target-nums[i]],i])
            else:
                dic.setdefault(nums[i],i)


s=Solution()
print(s.twoSum([1,2,3,4,5],8))