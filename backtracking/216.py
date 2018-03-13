class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []


        def deeper(path, target, start_element):
            print(path, target, start_element)
            if target == 0 and len(path) == k:
                res.append(path)

            for e in range(start_element, 10):
                if target - e >= 0:
                    deeper(path + [e], target  - e, e + 1)

        deeper([], n, 1)
        return res

s = Solution()
res = s.combinationSum3(3,9)
print(res)