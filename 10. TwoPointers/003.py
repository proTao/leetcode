class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0
        look_forward = [length] * length # lookup table to next position
        cache = {} # last_position
        for i, c in enumerate(s):
            if c in cache:
                look_forward[cache[c]] = i
            cache[c] = i
        del cache

        start = -1
        left = 0
        res = 0
        while left != length:
            left = start+1
            start = left
            if length - left <= res:
                break
            right = look_forward[left]
            while left != right:
                right = min(look_forward[left], right)
                left += 1
            res = max(res, right - start)
        return res

a = "abcabcbb"
# a = "pwwkew"
# a = "aa"
a = "dvdf"
# a = "a"
# a = ""
print(Solution().lengthOfLongestSubstring(a))

