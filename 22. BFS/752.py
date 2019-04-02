from typing import List
from collections import deque

operations = [lambda x: (x+1000)%10000,
             lambda x: x+100 if x%1000//100<9 else x-900,
             lambda x: x+10 if x%100//10<9 else x-90,
             lambda x: x+1 if x%10<9 else x-9,
             lambda x: (x+9000)%10000,
             lambda x: x-100 if x%1000//100>0 else x+900,
             lambda x: x-10 if x%100//10>0 else x+90,
             lambda x: x-1 if x%10>0 else x+9
            ]
def genNext(x, operations):
    for f in operations:
        yield f(x)


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(int(i) for i in deadends)
        if 0 in visited:
            return -1

        queue = deque([0])
        step = 1
        target = int(target)

        while queue:
            width = len(queue)
            for _ in range(width):
                cur = queue.popleft()
                for i in genNext(cur, operations):
                    if i not in visited:
                        if i == target:
                            return step
                        else:
                            visited.add(i)
                            queue.append(i)
                    
            step += 1
        return -1

if __name__ == "__main__":
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    deadends = ["8888"]
    target = "0009"
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"
    deadends = ["0000"]
    target = "8888"
    print(Solution().openLock(deadends, target))