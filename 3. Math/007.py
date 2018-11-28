class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        s = str(x)
        flag = False
        if s[0] == '-':
            flag = True
            s = s[1:]
        s = s[::-1]
        res = int(s)*(-1) if flag else int(s)
        if res>=2**31 or res<0-2**31:
            return 0
        else:
            return res
        

print(Solution().reverse(1534236469))