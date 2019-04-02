from collections import Counter
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return Counter(A).most_common(1)[0][0]
        # num = None
        # cnt = 0
        # for n in A:
        #     if cnt == 0:
        #         num = n
        #         cnt = 1
        #         continue
        #     if n == num:
        #         cnt += 1
        #     else:
        #         cnt -= 1
        # return num


if __name__ == "__main__":
    a = [2,1,2,5,3,2]
    print(Solution().repeatedNTimes(a))