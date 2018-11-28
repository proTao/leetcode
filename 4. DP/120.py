import math
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        l1 = [math.inf] * len(triangle)
        l2 = [math.inf] * len(triangle)
        l1[0] = triangle[0][0]

        i = 1
        for layer in triangle[1:]:
            print(i,layer)
            length = len(layer)
            if i % 2 == 1:
                l2[0] = l1[0] + layer[0]
                l2[length-1] = l1[length-2] + layer[length-1]
                for j in range(1, length-1):
                    l2[j] = layer[j]+min(l1[j], l1[j-1])
            else:
                l1[0] = l2[0] + layer[0]
                l1[length-1] = l2[length-2] + layer[length-1]
                for j in range(1, length-1):
                    l1[j] = layer[j]+min(l2[j], l2[j-1])
            i+=1

        # print("l1",l1)
        # print("l2",l2)
        # print(i)
        return min(l2) if i%2==0 else min(l1)
        


triangle=[[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],[-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],[-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]
s = Solution()
print(s.minimumTotal(triangle))
