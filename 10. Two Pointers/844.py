class Solution:
    def main(self, s1, s2):
        l1 = []
        for i in s1:
            if i is '#':
                l1.pop()
            else:
                l1.append(i)
        l2 = []
        for i in s2:
            if i is '#':
                l2.pop()
            else:
                l2.append(i)
        return "".join(l1) == "".join(l2)

print(Solution().main("a#b#","c#d#"))