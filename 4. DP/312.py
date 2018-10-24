from itertools import permutations
from collections import Counter
class Solution:
    def process5(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mi = -1
        mn = -1
        for i,n in enumerate(nums):
            if i==0:
                plus = nums[0] * nums[-1]
            elif i == len(nums)-1:
                plus = nums[-1] * nums[-2]
            else:
                plus = nums[i-1]*nums[i]*nums[i+1]

            temp = self.process4(nums[:i]+nums[i+1:]) + plus
            if mn < temp:
                mn = temp
                mi = n
        print(mi,":",mn, nums)
        return mi

    def process4(self, nums):
        mi = -1
        mn = -1
        for i,n in enumerate(nums):
            if i==0:
                plus = nums[0] * nums[-1]
            elif i == len(nums)-1:
                plus = nums[-1] * nums[-2]
            else:
                plus = nums[i-1]*nums[i]*nums[i+1]

            temp = self.process3(nums[:i]+nums[i+1:]) + plus
            if mn < temp:
                mn = temp
                mi = n
        # print(mi,":",mn, nums)
        return mn

    def process3(self, nums):
        a,b,c=nums
        # print("a:ab+bc+max(b,c)",a*b+b*c+max(b,c))
        # print("b:abc+ac+max(a,c)",a*b*c+a*c+max(a,c))
        # print("c:bc+ab+max(a,b)",b*c+a*b+max(a,b))
        return max(a*b+b*c+max(b,c), a*b*c+a*c+max(a,c), b*c+a*b+max(a,b))

s=Solution()
nums=[1,2,3,4,5]
res = []
for i in permutations(nums):
    res.append(s.process5(i))
print(Counter(res))
