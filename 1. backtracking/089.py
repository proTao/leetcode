class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        DEBUG = False
        # initial
        res = [0]
        if n == 0:
            return [0]
        # res.append([0 for i in range(n)])

        # times
        plus = 1
        for i in range(n):
            # how many time to clip and time the code table
            l = len(res)
            # copy
            for j in range(l-1, -1, -1):
                res.append(res[j]) # must copy
            if DEBUG:
                print("copy period of ",i,res)

            # clip bit ( by add plus )
            for j in range(l, l*2):
                res[j] += plus # change n-1-i to i is also just ok
            if DEBUG:
                print("copy period of ",i,res)
            plus *= 2
        return res

s = Solution()
res = s.grayCode(3)
print(res)

