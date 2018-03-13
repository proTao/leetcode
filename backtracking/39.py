class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        # input is a set
        # distinct_candidates = set(candidates)


        # assume that candidates is already sorted

        def deeper(path, target, start_position):
            # print(path, target, start_position)
            if target == 0:
                res.append(path)
                return


            for i in range(start_position, len(candidates)):
                if target - candidates[i] >= 0:
                    deeper(path + [candidates[i]], target - candidates[i], i)

        deeper([], target, 0)

        return res

s = Solution()
res = s.combinationSum([1,2,3,6,7,9,10,11,12,133,14,15,16], 60)

print(len(res))