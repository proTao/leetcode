import bisect

class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res = []
        A = sorted(A)
        for b in B:
            index = bisect.bisect_right(A,b)
            if index >= len(A): 
                a = A.pop(0)
            else:
                a = A.pop(index)
            print(a,'->',b)
            res.append(a)
        return res
A = [12,24,8,32]
B = [13,25,32,11]
print(Solution().advantageCount(A, B))
