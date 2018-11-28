class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dic = {c:i for i,c in enumerate(S)} # good job!
        start = 0
        end = 0
        res = []
        for i in range(len(S)):
            end = max(end, dic[S[i]])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
