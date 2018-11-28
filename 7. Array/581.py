class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
	# 相当于solution中的Approach 5
        l_bound = len(nums)-1

        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                l_bound = i
                break



        r_bound = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i]<nums[i-1]:
                r_bound = i
                break

        if r_bound <= l_bound:
            print("ok")
            return 0

        max_inner = max(nums[l_bound:r_bound+1])
        min_inner = min(nums[l_bound:r_bound+1])


        while(l_bound > 0 and min_inner < nums[l_bound-1]):
            l_bound -= 1
        while(r_bound < len(nums)-1 and max_inner > nums[r_bound+1]):
            r_bound += 1


        print(l_bound, r_bound)
        return r_bound - l_bound + 1
s=Solution()

print(s.findUnsortedSubarray([2,6,4,8,10,9,15]))
print(s.findUnsortedSubarray([5,1,2,3,4]))
print(s.findUnsortedSubarray([1,2]))
print(s.findUnsortedSubarray([1]))
print(s.findUnsortedSubarray([1,5,1,2,3,4,5]))
print(s.findUnsortedSubarray([1,2,4,5,3]))



