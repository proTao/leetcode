class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        if len(s) == 0:
            return res
        def deeper(path, start):
            print(path, start)
            if len("".join(path)) == len(s):
                print("--------------solution:",path)
                res.append(path)
                return

            for i in range(start+1,len(s)+1):
                # judge palindrome
                substr = s[start:i]
                is_palindrome = True
                for j in range(len(substr)//2):
                    if substr[j] != substr[-1-j]:
                        is_palindrome = False
                        break

                if is_palindrome:
                    deeper(path+[substr], i)

        deeper([], 0)
        return res

s = Solution()
res = s.partition("aabbcc")
print(res)
