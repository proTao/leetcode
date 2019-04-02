class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left_max = [A[0]]
        for a in A[1:]:
            left_max.append(max(left_max[-1], a))
            # print(left_max)

        right_min = [None] * len(A)
        right_min[-1] = A[-1]

        for i in range(len(A)-2, -1, -1):
            right_min[i] = min(right_min[i+1], A[i])
        
        for i in range(len(A)-1):
            if left_max[i] <= right_min[i+1]:
                return i + 1
        assert False
        

l = [1,1,1]
print(Solution().partitionDisjoint(l))
