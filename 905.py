class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        length = len(A)
        if length <= 1:
            return A
        fast = slow = 0
        while True:
            while fast < length and A[fast] % 2 == 1:
                fast += 1
            if fast == length:
                break
            A[fast], A[slow] = A[slow], A[fast]
            fast += 1
            slow += 1
        
        return A

a = [3]
print(Solution().sortArrayByParity(a))
        