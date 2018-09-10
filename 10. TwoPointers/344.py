class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # best answer
        # return s[::-1]
        l = list(s)
        i = 0
        j = len(s)-1
        while i < j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
        return "".join(l)

print(Solution().reverseString("applr"))