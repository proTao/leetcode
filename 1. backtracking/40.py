class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # initial
        res = []
        sorted_candidates = sorted(candidates)

        def deeper(path, target, start_position):
            if target == 0:
                res.append(path)

            last_element = -1
            for i in range(start_position, len(candidates)):
                if target - sorted_candidates[i] >= 0:
                    if last_element != sorted_candidates[i]:
                        deeper(path + [sorted_candidates[i]], target - sorted_candidates[i], i+1)
                        last_element = sorted_candidates[i]
        
        deeper([], target, 0)
        return res

s = Solution()
res = s.combinationSum2([], 1)
print(res)


    





""" old divide method
class Solution(object):
    def combinationSum2(self, candidates, target):
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
"""