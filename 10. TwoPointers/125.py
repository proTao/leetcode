class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str1 = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = str.lower(str(s))
        s = [w for w in s if w in str1]
        rs = s[::-1]
        if rs == s:
            return True
        return False

print(Solution().isPalindrome('a.'))