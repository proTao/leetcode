import bisect
inf = float("inf")
class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # 


        # initial
        index = 0
        max_dict = 0
        direct = 0
        up_obstc = {}
        right_obstc = {}
        for x, y in obstacles:
            if x not in up_obstc:
                up_obstc[x] = []
            if y not in right_obstc:
                right_obstc[y] = []
            bisect.insort(up_obstc[x], y)
            bisect.insort(right_obstc[y], x)
        x=y=0
        print(x,y)

        # 
        def changeDirect():
            nonlocal index
            nonlocal direct
            while commands[index] < 0:
                if commands[index] == -1:
                    direct += 1
                else:
                    direct -= 1
                index += 1

        def getDist():
            nonlocal index
            nonlocal x
            nonlocal y
            res = 0
            while index < len(commands) and commands[index] > 0:
                res += commands[index]
                index += 1

            if direct == 0:
                if x in up_obstc:
                    obs_index = bisect.bisect(up_obstc[x]+[inf], y)
                    obs = up_obstc[x][obs_index] if obs_index < len(up_obstc[x]) else float("inf")
                    y = min(y + res, obs - 1)
                else:
                    y += res
            elif direct == 1:
                if y in right_obstc:
                    obs_index = bisect.bisect(right_obstc[y]+[inf], x)
                    obs = right_obstc[y][obs_index] if obs_index < len(right_obstc[y]) else float("inf")
                    x = min(x + res, obs - 1)
                else:
                    x += res
            else:
                print("Direction Error")

        # try
        print(x,y)
        while index < len(commands):
            if commands[index] < 0:
                print("change direction")
                changeDirect()
                print(direct)
            else:
                print("get new position")
                getDist()
                max_dict = max(max_dict, x**2+y**2)
                print(x,y)
        return max_dict

class Solution(object):
    def robotSim(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  #left
                di = (di - 1) % 4
            elif cmd == -1:  #right
                di = (di + 1) % 4
            else:
                for k in xrange(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)

        return ans

commands = [-2,8,3,7,-1]
obstacles = [[-4,-1],[1,-1],[1,4],[5,0],[4,5],[-2,-1],[2,-5],[5,1],[-3,-1],[5,-3]]
print(Solution().robotSim(commands, obstacles))