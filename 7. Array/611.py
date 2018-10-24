class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # time is too long
        # nums.sort()
        # count = 0

        # for i1 in range(0, len(nums)-2):
        #     for i2 in range(i1+1,len(nums)-1):
        #         for i3 in range(i2+1,len(nums)):
        #             if nums[i1] + nums[i2] > nums[i3]:
        #                 count += 1
        #                 # print(nums[i1],nums[i2],nums[i3],"OK")
        #             else:
        #                 # print(nums[i1],nums[i2],nums[i3],"no")
        #                 break


        # return count

        nums.sort()
        count = 0
        max_element = nums[-1]
        # print(max_element)
        for i1 in range(0, len(nums)-2):
            # print("i:",i1)
            for i2 in range(i1+1,len(nums)-1):
                # print("j:",i2)
                bound = nums[i1] + nums[i2]
                if bound > max_element:
                    bound_position = len(nums)
                else:
                    while(bound not in nums[i2+1:]):
                        bound += 1
                    bound_position  = nums.index(bound, i2+1)
                addition = bound_position - i2 - 1
                count += addition
                print(nums[i1],nums[i2],nums[bound_position-1],addition)

        return count

s=Solution()
print(s.triangleNumber([1,2,2,3,4,6]))
print(s.triangleNumber([0,0,0]))
print(s.triangleNumber([0,1,0]))