class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_r = int(a.split("+")[0])
        a_i = int(a.split("+")[1][:-1])
        b_r = int(b.split("+")[0])
        b_i = int(b.split("+")[1][:-1])

        result_r = a_r * b_r - a_i * b_i
        result_i = a_i * b_r + a_r * b_i
        return str(result_r) + "+" + str(result_i) + "i"

s=Solution()
a="1+1i"
b="1+1i"
print(s.complexNumberMultiply(a,b))
a="1+-1i"
b="1+-1i"
print(s.complexNumberMultiply(a,b))
