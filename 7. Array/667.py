class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        lowest = 1
        highest = n
        is_even = True
        while(k):
            if is_even:
                res.append(lowest)
                lowest += 1
                is_even = False
            else:
                res.append(highest)
                highest -= 1
                is_even = True
            k -= 1
        if not is_even:
            res.extend(list(range(lowest, highest+1, 1)))
        else:
            res.extend(list(range(highest, lowest-1, -1)))
        return res

s = Solution()
res = s.constructArray(5,2)
print(res)