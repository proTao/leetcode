from typing import List
from pprint import pprint

prime = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        index_map = {}
        for s in strs:
            key = 1
            for c in s:
                key *= prime[ord(c)-97]
            
            if key in index_map:
                res[index_map[key]].append(s)
            else:
                index_map[key] = len(res)
                res.append([s])
            
        return res


if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    pprint(Solution().groupAnagrams(strs))