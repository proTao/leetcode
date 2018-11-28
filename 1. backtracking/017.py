class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        # initial
        mapping = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        res = []

        # border situation
        if digits == "":
            return res


        def deeper(path, i):
            """
            i: current index of digits
            """
            print(path,i)
            if i == len(digits):
                res.append(path)
                return
            
            for c in mapping[digits[i]]:
                deeper(path+c, i+1)

        deeper("", 0)
        return res

s = Solution()
res = s.letterCombinations("23")
print(res)