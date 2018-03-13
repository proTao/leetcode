class Solution:

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0
        res = []
        

        def deeper(path, remain):
            # 保证path中没有重复元素
            print([path], remain)
            if remain == 0:
                return 0

            # return condition
            # for i in path :
            #     return 10**(remain-1)

            # 
            for i in [1,2,3,4,5,6,7,8,9,0]:
                if str(i) not in path:
                    x = str(i)
                    break

            if len(path) == 0:
                return 9 * deeper(path+x, remain-1)
            else:
                return (10-len(path)) * deeper(path+x, remain-1) + len(path) * 10 ** (remain-1)

        
        for i in range(1,n+1):
            count += deeper("",i)
        # print(res)
        return 10**n-count
        

        

s=Solution()
res = s.countNumbersWithUniqueDigits(6)
print(res)