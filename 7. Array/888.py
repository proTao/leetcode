class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = sum(A)
        sumB = sum(B)
        swap = False
        # make A > B
        if sumB > sumA:
            A, B = B, A
            sumA, sumB = sumB, sumA
            swap = True
        A.sort(reverse=True)
        B.sort()
        delta = (sumA - sumB)//2
        i = 0
        j = len(B) - 1

        while True:
            change_delta = A[i] - B[j]
            if change_delta == delta:
                if not swap:
                    return A[i], B[j]
                else:
                    return B[j], A[i]
            elif change_delta > delta:
                i += 1
            else:
                j -= 1

A = [1,2,5]
B = [2,4,6]
print(Solution().fairCandySwap(A, B))
        
        