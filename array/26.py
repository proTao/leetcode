class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=0
        length = len(nums)
        count_duplicates = 0
        
        while i<length:
            while j+1 < length and nums[j] == nums[j+1]:
                j += 1
            nums[i] = nums[j]
            i += 1
            j += 1
            print(i,j,nums)
            if j==length:
                return i
            


            
           

    

s=Solution()
nums = [1,2,2,2,3,4,4,5,5]
print(nums)
print(s.removeDuplicates(nums))