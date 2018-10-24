from pprint import pprint
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.old_color = image[sr][sc]
        self.new_color = newColor
        self.image = image
        self.visited = [[False for i in range(len(image[0]))] for j in range(len(image))]
        self.visited[sr][sc] = True

        def dfs(image, sr, sc):
            print(sr,sc)
            print(self.visited)
            if sr-1>=0 and not self.visited[sr-1][sc] and image[sr-1][sc]==self.old_color:
                self.visited[sr-1][sc] = True
                dfs(image,sr-1,sc)
            if sr+1<len(image) and not self.visited[sr+1][sc] and image[sr+1][sc]==self.old_color:
                self.visited[sr+1][sc] = True
                dfs(image,sr+1,sc)
            if sc-1>=0 and not self.visited[sr][sc-1] and image[sr][sc-1]==self.old_color:
                self.visited[sr][sc-1] = True
                dfs(image,sr,sc-1)
            if sc+1<len(image[0]) and not self.visited[sr][sc+1] and image[sr][sc+1]==self.old_color:
                self.visited[sr][sc+1] = True
                dfs(image,sr,sc+1)

            if image[sr][sc] == self.old_color:
                self.image[sr][sc] = newColor
                

        dfs(image,sr,sc)
        return self.image
s = Solution()
res = s.floodFill( [[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
print(res)