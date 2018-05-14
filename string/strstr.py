class Strstr:
    def Sunday(self, s, t):
        """
        s: source
        t: target
        """
        pass

    def KMP(self, s, t):
        trans = [0] # next

        # preprocess
        max_subfix_len = 0
        for char in t[1:]:
            while char != t[max_subfix_len]:
                max_subfix_len = t[max_subfix_len]
            if char == t[max_subfix_len]: