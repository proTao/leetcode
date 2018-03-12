class Solution(object):
    def __init__(self):
        self.res = []

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        # initial
        res = []
        position = []
        for i in range(len(S)-1,-1,-1):
            if S[i].isalpha():
                position.append(i)
            
        # print(position)

        def helper(path, current):
            # return codition
            print(path, current, position)
            if len(position) == 0:
                res.append(path+S[current+1:])
                return

            # prepare to next layer
            next_chr_position = position.pop()

            # all the situation of next layer
            upper = S[next_chr_position].upper()
            lower = S[next_chr_position].lower()
            helper(path+S[current+1:next_chr_position] + upper,\
                    next_chr_position)
            helper(path+S[current+1:next_chr_position] + lower, \
                    next_chr_position)
            
            # return to current layer
            position.append(next_chr_position)

        helper("",-1)
        return res

    def letterCasePermutation2(self, S):
        res = []

        if len(S) == 0:
            return [""]

        # initial
        head = []
        for i in range(len(S)):
            if S[i].isdigit():
                head.append(S[i])
            else:
                break
        else:
            # handle all the char in S is digit
            i += 1
        res.append(head)
        # res.append(S[:i])
        # print("head:", res)
        # now i is point to the first alpha
        for i in range(i, len(S)):
            if S[i].isdigit():
                for s in res:
                    s.append(S[i])
                # print("digit:", res)
            else:
                l = len(res)
                for j in range(l):
                    res.append(res[j].copy())  # copy is important
                    res[j].append(S[i].lower())
                for j in range(l, 2*l):
                    res[j].append(S[i].upper())
                # print("alpha:", res)

            # print(S[i])
        for i in range(len(res)):
            res[i] = "".join(res[i])
        return res

s = Solution()
res = s.letterCasePermutation("ab")
print(res)
