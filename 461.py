class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        diff = x^y
        count = 0
        while diff:
            # print(diff)
            if(diff % 2 == 1):
                count +=1
                # print("aha")
            diff = diff // 2
        return count

s=Solution()
print(s.hammingDistance(10,0))