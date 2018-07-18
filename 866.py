# high = 100000000
def checkPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True

def checkPalindrome(n):
    s = str(n)
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False

    return True

def getNextPalidrome(n):
    if n < 9:
        return n+1
    s = str(n)
    l = len(s)
    j = l//2-1
    while j >= 0:
        s = str(n)
        for i in range(l//2):
            if s[l-1-i] < s[i]:
                return int(s[:l-1-i]+"".join(reversed(s[0:i+1])))
        if l % 2 == 1 and s[l//2] < '9':
            return int(s[:l//2]+str(int(s[l//2])+1)+"".join(reversed(s[:l//2])))
        if s[0] == '9':
            j -= 1
        else:
            n += 10 ** (l-1-j)
            n -= n % 10 ** (l-1-j)
            print("----",n)


    # print(l)
    return 10 ** l + 1



jump = {}
class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """

        if checkPalindrome(N) and checkPrime(N):
            return N
        i = N
        while True:
            i = getNextPalidrome(i)
            if checkPrime(i):
                return i





# print(checkPrime(1))
print(getNextPalidrome(1100))

print(Solution().primePalindrome(930))
