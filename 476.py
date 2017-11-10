class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 找到比num大的最小的低位是连续的1的数
	# 用这个数作为异或的掩模
        mod = 1
        while num >= mod:
            mod *= 2
        return num ^ (mod-1)

s=Solution()
print(s.findComplement(5))
