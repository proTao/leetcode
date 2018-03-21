class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        tail_io_nums = 0
        res = []
        # preprocessing suffix
        # order = s
        # while order[-1:] == ")":
        #     i = len(order)-2
        #     while i >= 0 and order[i] != ")":
        #         if order[i] == "(":
        #             tail_io_nums += len(order) - i
        #             order = order[:i]
        #             break
        #         i -= 1
        #     else:
        #         break
        self.order = s

        def deeper(current_order, i_count, o_count, i):
            print(current_order, i_count, o_count, i)
            if i == len(self.order):
                if i_count == o_count:
                    res.append(current_order)
            if o_count > i_count:
                last_j = -1
                for j in range(len(current_order)):
                    if current_order[j] == ")":
                        if j-1 != last_j:
                            deeper(current_order[:j]+current_order[j+1:], i_count, o_count-1, i)
                        last_j = j
            elif i<len(self.order):
                next_char = self.order[i]
                if next_char == "(":
                    deeper(current_order+next_char, i_count+1, o_count, i+1)
                elif next_char == ")":
                    deeper(current_order+next_char, i_count, o_count+1, i+1)
                else:
                    deeper(current_order+next_char, i_count, o_count, i+1)

        deeper("", 0, 0, 0)
        print(res)
        if tail_io_nums > 0:
            return [i+s[tail_io_nums*(-1):] for i in res] or [""]
        else:
            return res or [""]
        

s = ")(f"
print(Solution().removeInvalidParentheses(s))
