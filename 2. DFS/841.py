from collections import deque
from typing import List




class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        have_keys = set([0])
        queue = deque([0])

        def getNeighbor(cur):
            for i in rooms[cur]:
                yield i


        while queue:
            cur = queue.popleft()
            for neighbor in getNeighbor(cur):
                if neighbor not in have_keys:
                    have_keys.add(neighbor)
                    queue.append(neighbor)
        return len(have_keys) == len(rooms)

if __name__ == "__main__":
    a = [[1,3],[3,0,1],[2],[0]]
    print(Solution().canVisitAllRooms(a))