class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(candidates)
        # if len(candidates)<=3:
        #     res = self.searchCombine(candidates, target)
        # else:
        res = self.split(candidates[:length//2], candidates[length//2:], target, False, True)

        return self.drop_duplicates(res)

    def split(self, left, right, target, debug=False, top_layer=False):
        '''
        return 2-D list
        '''
        if debug:
            print("into split")
            print(left,right,target)
        res = []
        for i in range(target+1):
            left_res = self.searchCombine(left, i, debug)
            right_res = self.searchCombine(right, target-i, debug)
            if((left_res or i==0) and (right_res or i==target)):
                # if top_layer:
                #     temp = []
                #     temp.extend(left_res)
                #     temp.extend(right_res)
                #     res.append(temp)
                # else:
                if i==0:
                    left_res=[[]]
                if i==target:
                    right_res=[[]]
                for i in left_res:
                    for j in right_res:
                        temp = []
                        temp.extend(i)
                        temp.extend(j)
                        res.append(temp)
                if debug:
                    print("answer!!",top_layer, temp)
        return res
    
    def searchCombine(self, candidates, target, debug=False):
        '''
        return 2-D list
        '''
        if debug:
            print("into search_combine")
            print(candidates,target)
        if target <= 0 or len(candidates)<1:
            return
        if len(candidates) == 2:
            if candidates[0] == target:
                return [[candidates[0]]]
            if candidates[1] == target:
                return [[candidates[1]]]
            if candidates[0]+candidates[1] == target:
                return [[candidates[0], candidates[1]]]
        elif len(candidates) == 1:
            if candidates[0] == target:
                return [[candidates[0]]]
        else:
            length = len(candidates)
            split_answer = self.split(candidates[:length//2], candidates[length//2:], target)
            # print("split_answer", split_answer)
            return split_answer

    def drop_duplicates(self, L):
        dic=set()
        length = len(L)
        i=0
        while i < length:
            # print(i,length,L)
            temp = hash(tuple(sorted(L[i])))
            if temp in dic:
                L.pop(i)
                length -= 1
            else:
                dic.add(temp)
                i += 1
        return L

'''别人的solution
class Solution(object):
    def combinationSum2(self, candidates, target):
        # Sorting is really helpful, se we can avoid over counting easily
        candidates.sort()                      
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result
        
    def combine_sum_2(self, nums, start, path, result, target):
        # Base case: if the sum of the path satisfies the target, we will consider 
        # it as a solution, and stop there
        if not target:
            result.append(path)
            return
        
        for i in xrange(start, len(nums)):
            # Very important here! We don't use `i > 0` because we always want 
            # to count the first element in this recursive step even if it is the same 
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if i > start and nums[i] == nums[i - 1]:
                continue

            # If the current element is bigger than the assigned target, there is 
            # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
                break

            # We change the start to `i + 1` because one element only could
            # be used once
            self.combine_sum_2(nums, i + 1, path + [nums[i]], 
                               result, target - nums[i])


s = Solution()
c = [1,1,2,3]
t = 5
print(s.combinationSum2(c,t))
'''
    

s = Solution()
c = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
t = 27

res = s.combinationSum2(c,t)
print(res)
