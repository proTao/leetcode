class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        change = [1] * len(A)
        not_change = [0] * len(A)

        for i, (a,b) in enumerate(zip(A[1:], B[1:])):
            print(a,b)
            would_not_change = a > A[i] and b > B[i]
            can_change = b > A[i] and a > B[i]
            if can_change and would_not_change:
                print("both")
                not_change[i+1] = min(change[i], not_change[i])
                change[i+1] = not_change[i] + 1
            elif can_change:
                # must change
                print("change")
                not_change[i+1] = change[i]
                change[i+1] = not_change[i] + 1
            elif would_not_change:
                # can't change
                print("not change")
                not_change[i+1] = not_change[i]
                change[i+1] = change[i] + 1
            else:
                # impossible
                raise Exception("impossible")

        print(change)
        print(not_change)
        return min(change[-1], not_change[-1])



A=[0,7,8,10,10,11,12,13,19,18]
B=[4,4,5,7,11,14,15,16,17,20]
print(Solution().minSwap(A, B))
