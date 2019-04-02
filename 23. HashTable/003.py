class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 1
        chr2idx = {s[0]:0}
        start_idx = 0
        for i, c in enumerate(s[1:], start=1):
            if c not in chr2idx:
                if i-start_idx+1 > max_len:
                    max_len = i-start_idx+1
            else:
                end_idx = chr2idx[c]+1
                for j in range(start_idx, end_idx):
                    del chr2idx[s[j]]
                start_idx = end_idx
            chr2idx[c] = i
        return max_len

if __name__ == "__main__":
    s = "dvdf"
    print(Solution().lengthOfLongestSubstring(s))
