class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) == 0:
            return []
        length = len(A)
        even = 0
        odd = 1
        while True:
            while even<length and A[even]%2 == 0:
                even += 2
            while odd<length and A[odd]%2 == 1:
                odd += 2
            if even<length and odd<length: 
                A[even], A[odd] = A[odd], A[even]
            else:
                break

        return A

print(Solution().sortArrayByParityII([2,3,1,1,4,0,0,4,3,3]))