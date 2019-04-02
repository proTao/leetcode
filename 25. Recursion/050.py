class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        if n <= 0:
            return self.myPow(1/x, -n)
        if n == 1:
            return x
        
        temp = self.myPow(x, n//2)
        if n % 2 == 0:
            return temp ** 2
        else:
            return temp ** 2 * x

if __name__ == "__main__":
    print(Solution().myPow(2.00000, -2))