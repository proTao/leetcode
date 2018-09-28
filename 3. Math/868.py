class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        l = len(bin(N)[2:])
        position = -1
        while l > 0 :

            if N % 2 == 1:
                if position == -1:
                    position = l
                    max_gap = 0
                else:
                    # print(N, l, position)
                    max_gap = max(max_gap, position - l)
                    position = l
            N = N // 2
            l -= 1
        return max_gap

print(Solution().binaryGap(1))