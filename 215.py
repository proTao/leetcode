import random
class Solution(object):
    def findKthLargest(self, nums, k):
        print("target : " + str(k) + "th")
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # space: O(k)
        # can not AC

        # sort_k = [float("-inf") for i in range(k)]

        # for element in nums:
        #     # print(element)
        #     # print(nums[-1])
        #     if element > sort_k[-1]:
        #         sort_k[-1] = element
        #     for i in range(k-2,-1,-1):
        #         if element > sort_k[i]:
        #             sort_k[i+1] = sort_k[i]
        #             sort_k[i] = element
        #     # print(sort_k)
        # return sort_k[-1]


        threshold = 3
        # by sorted, can AC 
        if len(nums) <= threshold:
            n=len(nums)
            a=sorted(nums)
            return a[n-k]
        else:
        # quite select by partition

        # select a pivot
            index1 = random.randrange(0, len(nums)-1)
            index2 = random.randrange(0, len(nums)-1)
            index3 = random.randrange(0,len(nums)-1)
            
            if index1 > index2 and index1 < index3 or index1 > index3 and index1 < index2:
                pivot = index1
            elif index2 > index1 and index2 < index3 or index2 > index3 and index2 < index1:
                pivot = index2
            else:
                # maybe has the same pivot
                pivot = index3
            print(nums[pivot])
            # make the pivot at the first position
            nums[0], nums[pivot] = nums[pivot], nums[0]

            # patition : bigger in the left and smaller in the right
            i = 1
            j = len(nums)-1
            while True:
                while(nums[j] < nums[0] and j > 0):
                    j -= 1
                while(nums[i] > nums[0] and i < len(nums)-1):
                    i += 1
                if i >= j:
                    break
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
            nums[0],nums[j] = nums[j],nums[0]

            print(nums)

            # recursion
            if j+1 == k:
                print("situation 1")
                return nums[j]
            if j+1 > k:
                print("situation 2")
                return self.findKthLargest(nums[:j],k)
            if j+1 < k:
                print("situation 3")
                return self.findKthLargest(nums[j+1:],k-j-1)
            

s=Solution()
print(s.findKthLargest([3,3,3,3,3,3,3,3,3,3,3],1))