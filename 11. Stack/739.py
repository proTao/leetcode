class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        min_index = []
        for i, val in enumerate(temperatures):
            if not min_index or val <= temperatures[min_index[-1]]:
                min_index.append(i)
            else:
                while min_index and temperatures[min_index[-1]] < val:
                    j = min_index.pop()
                    res[j] = i - j
                min_index.append(i)
        return res

a = [73,74,75,71,69,72,76,73] # [1, 1, 4, 2, 1, 1, 0, 0]
print(Solution().dailyTemperatures(a))