class Solution1:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [1] * (num + 1)
        res[0] = 0
        low = 2
        high = 4

        while low < num:
            print(low, high)
            for i in range(low + 1, min(high, num+1)):
                print(i)
                res[i] = res[i-low] + 1
            low = high
            high = high * 2

        return res

class Solution:
    def countBits(self, num):
        res = [0 for i in range(num+1)] 
        if num<=0 :
            return res
        res[1] = 1
        stage = 1
        for i in range(1, num+1):
            # f(5) = f(4) + f(1)
            # f(x) = f(x) + f()
            # res[i] = res[i%2] + res[i>>1]
            if i == stage * 2:
                stage *= 2
            res[i] = res[i-stage] + 1
        return res
print(Solution().countBits(10))
