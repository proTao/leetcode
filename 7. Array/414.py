class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = -float("inf")
        second = -float("inf")
        third = -float("inf")


        for element in nums:

            # ignore reduplication
            if element == third or element == second or element == first:
                continue

            # clear flag
            flag = -1

            # find the position
            if element > third:
                flag = 3
            if element > second:
                flag = 2
            if element > first:
                flag = 1

            # make it in his right position
            if flag == 1:
                third = second
                second = first
                first = element
            elif flag == 2:
                third = second
                second = element
            elif flag == 3:
                third = element
            # print(first, second, third)

        if third == -float('inf'):
            return first
        else:
            return third
s=Solution()
print(s.thirdMax([5,2,4,1,3,6,0]))
