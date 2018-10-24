from random import uniform
class Solution:

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self):
        """
        :rtype: List[float]
        """
        while True:
            x = uniform(-1, 1)
            y = uniform(-1, 1)
            if x**2 + y**2 <= 1:
                break
        return self.x + x * self.r, self.y + y * self.r



# Your Solution object will be instantiated and called as such:
obj = Solution(1,0,0)
print(obj.randPoint())