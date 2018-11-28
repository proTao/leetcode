from heapq import heapreplace, nlargest, heappush
def KthLargest(k, nums):
    heap = nlargest(k, nums)[::-1]
    delta = min(k, len(nums)) - k


    def _add(val):
        """
        :type val: int
        :rtype: int
        """
        nonlocal delta
        if delta < 0:
            heappush(heap, val)
            delta += 1
        elif val < heap[0]:
            pass
        else:
            heapreplace(heap, val)
        return heap[0]
        
    def inner():
        pass
    inner.add = _add
    return inner

# Your KthLargest object will be instantiated and called as such:
nums = [1]
k = 3
obj = KthLargest(k, nums)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
