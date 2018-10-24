class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s)-1
        vowels = set(('a','e','i','o','u','A','E','I','O','U'))
        l = list(s)
        while i < j:
            while i < j and l[i] not in vowels:
                i += 1
            while i < j and l[j] not in vowels:
                j -= 1
            if i < j:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
        return "".join(l)

print(Solution().reverseVowels("hello"))