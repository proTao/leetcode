class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            assert K == 1
            return 0
        
        father = self.kthGrammar(N-1, (K+1)//2)
        if father == 0:
            return 1 if K%2 == 0 else 0
        if father == 1:
            return 1 if K%2 == 1 else 0
        assert False

if __name__ == "__main__":
    print(Solution().kthGrammar(4,5))