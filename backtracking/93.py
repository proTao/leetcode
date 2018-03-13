class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        length = len(s)
        def deeper(path, field_count, rest_length):
            # return condition
            if field_count == 4 and rest_length == 0:
                res.append(".".join(path))

            # Heuristic pruning to accelerate
            if (4 - field_count) * 3 < rest_length:
                return 

            # go deeper
            if rest_length >= 1:
                deeper(path+[s[length - rest_length : length - rest_length + 1]],\
                       field_count+1, rest_length-1)

            if rest_length >= 2 and \
                s[length - rest_length] != '0':
                deeper(path+[s[length - rest_length : length - rest_length + 2]],\
                       field_count+1,rest_length-2)

            if rest_length >= 3 \
                and int(s[length - rest_length : length - rest_length + 3]) <= 255 \
                and s[length - rest_length] != '0':
                deeper(path+[s[length - rest_length : length - rest_length + 3]],\
                       field_count+1, rest_length-3)
            
        deeper([], 0, length)
        return res

s = Solution()
res = s.restoreIpAddresses("010010")
print(res)