class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                if i - dic[nums[i]] <= k :
                    return True
                else:
                    dic[nums[i]] = i
            else:
                dic[nums[i]] = i
        return False

s=Solution()
print(s.containsNearbyDuplicate([1,0,1,1],1))