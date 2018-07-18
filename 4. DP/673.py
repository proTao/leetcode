class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
            
        length = [1] * len(nums)
        count = [1] * len(nums)

        for i, n in enumerate(nums[1:], start=1):
            l = 0
            c = 0
            find = False
            for j in range(i-1, -1, -1):
                if nums[j] < n :
                    find = True
                    if length[j] == l:
                        c += count[j]
                    elif length[j] > l:
                        c = count[j]
                        l = length[j]
            if find:
                length[i] = l + 1
                count[i] = c
            print("length :", length)
            print("count :", count)
            print()

        res_l = 1
        res_c = 1
        for l, c in zip(length[1:], count[1:]):
            if l > res_l:
                res_l = l
                res_c = c
            elif l == res_l:
                res_c += c
        return res_c


a = [1,3,5,4,7]
print(Solution().findNumberOfLIS(a))