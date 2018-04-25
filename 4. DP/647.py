from math import ceil

class Solution1:
    def countSubstrings(self, s):
        """
 type s: str
 rtype: int
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

def MySolution():
    def caller():
        pass
    def countSubstrings(s):
        # Manacher Start
        expand_s = "%#" + "#".join([i for i in s]) + "#&"
        radius = [1 for i in range(len(expand_s))]
        most_right = 0
        pivot = 0
        for i in range(2, len(expand_s)-2):
            if i <= most_right:
                # 下面注释那一段化简为这一句, 化简之前的性能只能打败百分之四十多,化简之后达到了应有的性能
                radius[i] = min(radius[2*pivot-i], radius[pivot] + pivot - i)

                """
                sym_i = pivot - (i - pivot)
                if radius[sym_i] < radius[pivot] - (pivot - sym_i):
                    radius[i] = radius[sym_i]
                    continue
                elif radius[sym_i] > radius[pivot] - (pivot - sym_i):
                    radius[i] = radius[pivot] - (pivot - sym_i)
                    continue
                else:
                    radius[i] = radius[sym_i]
                """
                
            while expand_s[i+radius[i]] == expand_s[i-radius[i]]:
                radius[i] += 1

            if i + radius[i] - 1 > most_right:
                most_right = i + radius[i] - 1
                pivot = i

            

        return sum(int(radius[i]/2) for i in range(len(radius)))

    caller.countSubstrings = countSubstrings
    return caller

class SolutionN:
    def countSubstrings(self, S):
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z

        return sum(int((v+1)/2) for v in manachers(S))

class SolutionN2(object):
     def countSubstrings(self, S):
         N = len(S)         
         ans = 0
         for center in range(2*N - 1):
             left = int(center / 2)
             right = left + center % 2
             while left >= 0 and right < N and S[left] == S[right]:
                 ans += 1
                 left -= 1
                 right += 1
         return ans


s = MySolution()
string = "aababa"
print(s.countSubstrings(string))
