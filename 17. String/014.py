from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        limit = min(map(len,strs))
        size = len(strs)
        flag = True # 本轮是否匹配
        i = 0
        while i < limit:
            for j in range(size-1):    
                if strs[j][i] != strs[j+1][i]:
                    flag = False
                    break
            if not flag:
                break
            i += 1
        return strs[0][:i]


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))