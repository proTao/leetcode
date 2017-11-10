
class Solution(object):
    def findFriend(self, i, M):
        """
        :type i: int
        :type M:  List[List[int]]
        :rtype: List[int]
        output one's friends numbers
        """ 
        return list(filter(lambda x: M[i][x]==1, range(len(M[i])) ))

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        total = len(M)
        friend_circle_num = 0

        has_scan = set()    # the people we have process
        circle = set()  # current friends circle
        new_friends=set() # the peoples need to be process later (like a queue)

        for i in range(total):
            if i not in has_scan:
                # find one people we never meet
                has_scan.add(i)
                friend_circle_num += 1
                circle.clear()
                circle.add(i)
                new_friends.add(i) # push into the queue

                while(len(new_friends)>0): # BFS
                    k=new_friends.pop()
                    for j in self.findFriend(k, M):
                        has_scan.add(j)
                        j_friends = self.findFriend(j, M)
                        new_friends.update(filter(lambda x: x not in has_scan, j_friends)) # push into the queue
                        print("newfriend",new_friends)

                        # in face, in this question we don't need the variable 'circle' because we just want to know how many not what
                        if(len(new_friends) > 0):
                            circle.update(new_friends)

                print("circle",circle)
        return friend_circle_num

    

s = Solution()
print(s.findCircleNum([[1,1,0], [1,1,1], [0,1,1]]))
