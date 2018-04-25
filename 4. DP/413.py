class Solution1:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        if len(A) == 0:
            return 0

        k = 1
        d = 0
        a = A[0]
        res = 0

        for x in A[1:]:
            if k == 1:
                k = 2
                d = x-a
                a = x
            else:
                if x-a == d:
                    k = k+1
                    a = x
                else:
                    k = 2
                    d = x-a
                    a = x
            if k >= 3:
                res += k - 2
            # print(k)
        return res
        # def subQ(x) -> (int, int, int):
        #     """
        #     input:
        #     x : 新的元素
        #     return:
        #     k : 上一个等差数列长度
        #     d : 公差
        #     a : 上一个元素值
        #     """
        #     nonlocal k, d, a
        #     if k == 1:
        #         k = 2
        #         d = x-a

class Solution:
    def numberOfArithmeticSlices(self, A):
        if len(A) <= 2:
            return 0
        # 上面的代码不Pythonic

        k, d, a, res = 2, A[1]-A[0], A[1], 0
        for x in A[2:]:
            k, d = (k+1, d) if x-a == d else (2, x-a)
            a = x
            if k >= 3:
                res += k - 2
        return res

            



s = Solution()
a=[1,2,3,4,3,2,1]
print(s.numberOfArithmeticSlices(a))