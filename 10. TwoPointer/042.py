class Solution:
    def trap0(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = height.copy()
        right = height.copy()
        for i in range(1, len(height)):
            left[i] = max(left[i-1], left[i])
        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i+1], right[i])
        
        return sum(min(l,r)-x for l, r, x in zip(left, right, height))
    
    def trap(self, height):
        left_max = 0
        left = 0
        right_max = 0
        right = len(height)-1
        res = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                res += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                res += right_max - height[right]
                right -= 1
        return res
                
            
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))