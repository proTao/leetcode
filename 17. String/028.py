

class Solution:
    def strStr(self, a: str, b: str) -> int:
        """
        Sunday Algorithm
        """
        len_a = len(a)
        len_b = len(b)
        if len_b == 0:
            return 0
        if len_a == 0:
            return -1
        self.buildJumpTable(b)
        position = 0

        while position < len_a:
            isMatch = self.match(a, b, position)
            if isMatch:
                break
            else:
                if position + len_b < len_a:
                    look_forward = a[position + len_b]
                    if look_forward in self.jump_table:
                        position += self.jump_table[look_forward]
                    else:
                        position += len_b
                else:
                    break
        if isMatch:
            return position
        else:
            return -1
            

    def buildJumpTable(self, s):
        jump_table = {}
        length = len(s)
        for i, c in enumerate(s):
            jump_table[c] = length - i
        self.jump_table = jump_table
    
    def match(self, a, b, position):
        """
        check if a match b at position 
        """
        len_a = len(a)
        len_b = len(b)
        i = position
        j = 0
        while i < len_a and j < len_b:
            if a[i] != b[j]:
                return False
            i += 1
            j += 1
        return j == len_b

if __name__ == "__main__":
    print(Solution().strStr('substring searching algorithm', "search"))
