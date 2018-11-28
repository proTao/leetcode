class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        max_area = 0
        while i < j:
            max_area = max(max_area, 
                        min(height[i], height[j]) * (j - i))
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return max_area

print(Solution().maxArea([1,2,4,3]))