class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 0:
            return False
        i = 0
        while(i<len(bits)):
            if i == len(bits) - 1:
                return True
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return False

s = Solution()
res = s.isOneBitCharacter([1,1,1,0])
print(res)