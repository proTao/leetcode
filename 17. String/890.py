class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def judge(s, pattern):
            if len(s) != len(pattern):
                return False
            else:
                permutation = {}
                used = set()
                for i in range(len(s)):
                    char = pattern[i]
                    if char in permutation:
                        if permutation[char] != s[i]:
                            return False
                    else:
                        if s[i] in used:
                            return False
                        permutation[char] = s[i]
                        used.add(s[i])
            return True
        res = []
        for word in words:
            if judge(word, pattern):
                res.append(word)
        return(res)

l = ["abc","deq","mee","aqq","dkd","ccc"]
p = "abb"
print(Solution().findAndReplacePattern(l,p))
