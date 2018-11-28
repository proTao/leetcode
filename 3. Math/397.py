class Solution(object):
    def chooseAddOrMinus(self, n):
	"""
	这个是关键函数，判断一个奇数是应该加一还是减一
	判断的依据是哪个数能除以更多的2
	原理在于目的是最快的把一个数减小为1,除法总是更快一些
	惟一的例外是3,特殊之处在于3+1和3-1都是2的整数次幂
        :type n: int
        :rtype: int(1/-1)
        """

        if(n==3):
            return -1

        add = n+1
        minus = n-1
        
        while(True):
            if add%2==0 and minus%2==0:
                add /= 2
                minus /=2
            else:
                if add%2 == 0 :
                    return 1
                else:
                    return -1

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        step_count = 0

        while(n != 1):
            step_count += 1
            if n % 2 == 0:
                n = n / 2
            else:
                n += self.chooseAddOrMinus(n)
        return step_count

s=Solution()
print(s.integerReplacement(8))
print(s.integerReplacement(7))
print(s.integerReplacement(11))
