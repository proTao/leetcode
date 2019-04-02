class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def core(s, i, j):
            if j-i>=1:
                s[i], s[j] = s[j], s[i]
                core(s, i+1, j-1)
        core(s, 0,len(s)-1)

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7]
    Solution().reverseString(a)
    print(a)