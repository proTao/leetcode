class Solution:
    def findLongestWord(self, s, d:list):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        dic = {}
        for i, c in enumerate(s):
            if c not in dic:
                dic[c] = [i]
            else:
                dic[c].append(i)
        
        res = ""
        max_len = 0
        for word in d:
            if len(word) < max_len:
                continue
            index = -1
            count = {}
            for c in word:
                if c not in dic:
                    break
                if c not in count:
                    count_c = 0
                    count[c] = 1
                else:
                    count_c = count[c]
                    count[c] = count_c + 1
                while count_c < len(dic[c]):
                    if dic[c][count_c] <= index:
                        count_c += 1
                    else:
                        index = dic[c][count_c]
                        break
                else:
                    break
                    
            else:
                if len(word) == max_len:
                    if word < res:
                        res = word
                else:
                    res = word
                    max_len = len(word)
        return res


s = "abpcplea"
d = ["ale","apple","monkey","plea"]
s = "bab"
d = ["ba","ab","a","b"]
print(Solution().findLongestWord(s,d))
