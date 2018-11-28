class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        # initial
        pattern = []
        for e in p:
            if e == "*":
                pattern[-1] += "*"
                if len(pattern)>=2:
                    if pattern[-1] == pattern[-2] or \
                        pattern[-2] == ".*" and len(pattern[-1]) == 2:
                        pattern.pop()
                    elif pattern[-1] == ".*" and len(pattern[-2]) == 2:
                        pattern.pop()
                        pattern[-1] = ".*"
                    else:
                        pass
            else:
                pattern.append(e)


        def deeper(string, pattern):
            print("string:",string,",pattern:", pattern)
            if string == "" and (len(pattern) == 0 or len("".join(pattern)) == 2 * len(pattern)):
                return True

            if string == "" or len(pattern) == 0:
                return False

            min_match_length = 2 * len(pattern) - len("".join(pattern))
            if len(string) < min_match_length:
                return False
            # deeper to each branch
            match = False

            
            ## this is the first so i use lazy model
            ### situation1: "*" match nothing, and just skip
            if len(pattern[0]) == 2:
                match = deeper(string, pattern[1:])
                if match:
                    return True

            ### situation2: "x*" match only one x
            if pattern[0][0] == string[0] or pattern[0][0] == ".":
                match = deeper(string[1:], pattern[1:])
                if match:
                    return True


            ### situation3: "x*" match more than one x
            if len(pattern[0]) == 2 and (pattern[0][0] == "." or pattern[0][0] == string[0]):
                match = deeper(string[1:], pattern[:])
                if match:
                    return True



            return False
        return deeper(s,pattern)



s = Solution()
w="aaaaaaab"
p="a*a*a*a*a*a*a*c"



print(s.isMatch(w,p))

