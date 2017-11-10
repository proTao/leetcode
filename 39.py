class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sorted_candidates = sorted(candidates)
        return self.getSolution(sorted_candidates, target)

    def getSolution(self, candidates, target):
        """
        递归
        """
        solution_set = []
        if target in candidates:
            solution_set.append([target])

        # remove all the elements that bigger than target or equal with target
        candidates = filter(lambda x: x < target, candidates)
        candidates = list(candidates)

        for i in range(len(candidates)):
            print("current search by "+str(candidates[i])+", and go into deeper layer with target "+str(target - candidates[i]))
            sub_solutions = self.getSolution(candidates[i:], target - candidates[i])
            print("return from deeper layer with solution:")
            print(sub_solutions)
            for sub in sub_solutions:
                list_sub = sub
                list_sub.append(candidates[i])
                solution_set.append(list_sub)
        return solution_set

s=Solution()
print(s.combinationSum([1,2],3))
