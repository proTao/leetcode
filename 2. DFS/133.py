from typing import List
class Node:
    def __init__(self, val:int, neighbors:List):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        old2new = {}
        res = Node(node.val, [])
        old2new[node] = res
        stack = [node]

        while stack:
            node = stack.pop()
            if node.neighbors:
                for neighbor in node.neighbors:
                    if neighbor not in old2new:
                        old2new[neighbor] = Node(neighbor.val, [])
                        stack.append(neighbor)
                    old2new[node].neighbors.append(old2new[neighbor])
                        
        return res

        
if __name__ == "__main__":
    length = 7
    node = [None]*length
    for i in range(length):
        node[i] = Node(i, None)
    node[0].neighbors = [node[1]]
    node[1].neighbors = [node[0], node[2], node[3]]
    node[2].neighbors = [node[1], node[3]]
    node[3].neighbors = [node[1], node[2], node[4], node[5]]
    node[4].neighbors = [node[3], node[5], node[6]]
    node[5].neighbors = [node[3], node[4]]
    node[6].neighbors = [node[4]]
    Solution().cloneGraph(node[0])