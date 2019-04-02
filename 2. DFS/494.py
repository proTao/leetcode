from functools import lru_cache

class Solution:
    def findTargetSumWays1(self, nums, S):
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
                else:
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

        deeper(S, 1)
        return self.res

    def findTargetSumWays(self, nums, S):
        """
        第二次做的时候发现上面那个结果不对了是什么鬼
        """
        cache = {}
        @lru_cache(None, True)
        def dfs(rest_length, target):
            if rest_length == 1:
                if target == nums[0] or target == -nums[0]:
                    if target == 0:
                        return 2
                    else:
                        return 1
                else:
                    return 0
            

            rest_length -= 1
            lres = dfs(rest_length, target+nums[rest_length])
            rres = dfs(rest_length, target-nums[rest_length])
            rest_length += 1

            cache[(rest_length, target)] = lres+rres
            return lres+rres

        return dfs(len(nums), S)


print(Solution().findTargetSumWays([0],0))