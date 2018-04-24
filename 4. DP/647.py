from math import ceil

class Solution1:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        self.impossible_pivot = set()

        res = 0
        for i in range(1, len(s)+1):
            res = self.subQ(s[:i], res)
        return res


    def subQ(self, s, pre):
        k = len(s)
        print()
        print("sub question with '{}'".format(s))
        count = 0
        pivot_candidates = [i/2 for i in range(k-1, 2*k-2)]
        print(pivot_candidates)
        for pivot in pivot_candidates:
            if pivot not in self.impossible_pivot:
                is_palindromic =  self.judgePalindromic(pivot, k-1)
                print(is_palindromic)
                if is_palindromic:
                    count += 1
                else:
                    self.impossible_pivot.add(pivot)
        return pre + count + 1

    def judgePalindromic(self, pivot, right):
        left = int(2 * pivot - right)
        for i in range(ceil(pivot)-left):
            if self.s[left + i] != self.s[right - i]:
                return False
        return True


def Manacher(s):
    expand_s = "#" + "#".join([i for i in s]) + "#"
    maxlen = [1]
    for i in range(1, len(expand_s)):
        most_right = 0
        for j in range(0,i):
            most_right = j + maxlen[j] if j + maxlen[j] > most_right else most_right

    print(expand_s)

# s = Solution()
# string = "ababaa"
# print(s.countSubstrings(string))
Manacher("123")