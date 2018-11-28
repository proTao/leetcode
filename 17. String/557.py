class Solution(object):
    def reverseWord(self, word):
        return word[::-1]

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words = map(self.reverseWord, words)
        return(" ".join(words))

string="Let's take LeetCode contest"
s=Solution()
print(s.reverseWords(string))
