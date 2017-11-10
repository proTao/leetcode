class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # is the n_th element exist
        length = len(nums)
        n_flag = False
        for num in nums:
            print("process : "+str(num))
            if abs(num) == length:
                print("flag!")
                print(nums)
                n_flag = True
                continue

            
            nums[abs(num)] = -nums[abs(num)]
            
            print(nums)
            print("\n")

        if not n_flag:
            return length

        for i in range(length):
            if nums[i] > 0:
                return i
            if nums[i] == 0:
                cache = i
        else:
            return cache

s=Solution()
print(s.missingNumber([2,0]))