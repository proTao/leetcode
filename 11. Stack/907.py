from collections import deque
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = [0] * len(A)
        right = [len(A)-1] * len(A)

        stack = deque([0])
        for i, n in enumerate(A[1:], start=1):
            while stack and n < A[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]+1
            stack.append(i)

        stack.clear()
        stack.append(len(A)-1)
        for i in range(len(A)-2, -1, -1):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            if stack:
                right[i] = stack[-1]-1
            stack.append(i)

        res = 0
        count = []
        for i in range(len(A)):
            left_count = i - left[i] + 1
            right_count = right[i] - i + 1
            count.append(left_count * right_count)
            res += (left_count * right_count) * A[i]
        # print(left)
        # print(right)
        # print(A)
        # print(count)
        return res % (1000000007)
a=[3,1,2,4,1,5]
print(Solution().sumSubarrayMins(a))