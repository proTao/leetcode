class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chr_map = {}
        having_mapped = set()
        assert len(s) == len(t)
        for c1, c2 in zip(s, t):
            if c1 in chr_map:
                if chr_map[c1] != c2:
                    return False
            else: # c1 not in chr_map
                if c2 in having_mapped:
                    return False
                chr_map[c1] = c2
                having_mapped.add(c2)
        return True

if __name__ == "__main__":
    s = "paper"
    t = "title"
    print(Solution().isIsomorphic(s,t))