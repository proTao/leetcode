cache = {}
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.res = 0
        self.nums = sorted(nums, reverse = True)

        def deeper(target_sum, current_index):
            print(target_sum, current_index)
            # if (target_sum, current_index) in cache:
            #     print("hit")
            #     if cache[(target_sum, current_index)] == True:
            #         self.res += 1
            #     return cache[(target_sum, current_index)]

            if current_index == len(self.nums):
                if target_sum == 0:
                    self.res += 1
                    cache[(target_sum, current_index)] = True
                    return True
                cache[(target_sum, current_index)] = False
                return False

            flag = (len(nums) - current_index)*self.nums[current_index] >= abs(S - target_sum)
            if flag:
                res = deeper(target_sum - self.nums[current_index], current_index+1)
                if res == True:
                    cache[(target_sum, current_index)] = True
                    return True
                else:
                    res = deeper(target_sum + self.nums[current_index], current_index+1)
                    cache[(target_sum, current_index)] = res
                    return res




        deeper(S, 0)
        return self.res

print(Solution().findTargetSumWays([1,1,1,1,1],3))