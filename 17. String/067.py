class Solution:
    def addBinary1(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        res = [0] * (max(i,j)+1)
        carry = 0
        index = 0
        while i >= 0 and j >= 0:
            val = carry + int(a[i]) + int(b[j])
            carry = val // 2
            val = val % 2
            res[index] = val
            i -= 1
            j -= 1
            index += 1

        while i >= 0:
            val = carry + int(a[i])
            carry = val // 2
            val = val % 2
            res[index] = val
            i -= 1
            index += 1

        while j >= 0:
            val = carry + int(b[j])
            carry = val // 2
            val = val % 2
            res[index] = val
            j -= 1
            index += 1

        if carry:
            res.append(1)

        return "".join(map(str,res[::-1]))


    def addBinary(self, a, b):
        s = []
        c = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or c == 1:
            c += int(a[i]) if i >= 0 else 0
            c += int(b[j]) if j >= 0 else 0
            j -= 1
            i -= 1
            s.append(c%2)
            c //= 2

        return "".join(map(str,s[::-1]))

if __name__ == "__main__":
     a = "1010"
     b = "1011"
     print(Solution().addBinary(a,b))