class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves = moves.upper()

        U = moves.count("U")
        L = moves.count("L")
        R = moves.count("R")
        D = moves.count("D")
        print(U,L,R,D)
        if(U == D and L == R):
        	return True
        else:
        	return False

s=Solution()
print(s.judgeCircle("LL"))