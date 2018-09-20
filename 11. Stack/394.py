class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        ascii_9 = ord('9')


        continious_str_list = []
        repeat_num_list = []
        for i, c in enumerate(s):
            if ord(c) <= ascii_9:
                stack.append("".join(continious_str_list))
                # continious_str_list.clear()
                continious_str_list = []
                repeat_num_list.append(c)
            elif c == '[':
                stack.append(int("".join(repeat_num_list)))
                # repeat_num_list.clear()
                repeat_num_list = []
                stack.append(c)
            elif c == ']':
                temp_str = "".join(continious_str_list)
                # continious_str_list.clear()
                continious_str_list = []
                str_prefix = []
                pop_element = stack.pop()
                while pop_element!= "[":
                    str_prefix.append(pop_element)
                    pop_element = stack.pop()
                repeat_num = stack.pop()
                stack.append(("".join(str_prefix[::-1])+temp_str) * repeat_num)
            else:
                continious_str_list.append(c)
        
        if continious_str_list:
            stack.append("".join(continious_str_list))
        return  "".join(stack)





s = "3[a]2[bc]d" # return "aaabcbc".
s = "3[a2[c]]" # return "accaccacc".
s = "2[abc]1[c]ef" # return "abcabccdcdcdef".
print(Solution().decodeString(s))