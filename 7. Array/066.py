
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if carry == 0:
                break
            val = digits[i] + carry
            carry = val // 10
            digits[i] = val % 10
        if carry == 1:
            return [1] + digits
        else:
            return digits

if __name__ == "__main__":
    a = [9,9,9]
    print(Solution().plusOne(a))