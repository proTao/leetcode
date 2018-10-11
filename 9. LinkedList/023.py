from linkedtools import *

def heapify(l):
    length = len(l)
    for i in range(length//2, 0, -1):
        down(l, i, cmp_gt)

def up(l, i, cmp):
    # min_heap: cmp_lt
    while i > 0:
        if i//2 > 0 and cmp(l[i], l[i//2]):
            l[i], l[i//2] = l[i//2], l[i]
            i = i // 2
        else:
            break

def down(l, i, cmp):
    # min_heap: cmp_gt
    length = len(l)
    while i*2 < length:
        if i*2+1 >= length or cmp(l[i*2+1], l[i*2]):
            if cmp(l[i], l[i*2]):
                l[i], l[i*2] = l[i*2], l[i]
                i = i * 2
            else:
                break
        else:
            if cmp(l[i], l[i*2+1]):
                l[i], l[i*2+1] = l[i*2+1], l[i]
                i = i * 2 + 1
            else:
                break

def cmp_lt(a,b):
    if a.val < b.val:
        return True
    else:
        return False

def cmp_gt(a,b):
    if a.val > b.val:
        return True
    else:
        return False

def heappop(l):
    l[1], l[-1] = l[-1], l[1]
    res = l.pop()
    down(l, 1, cmp_gt)
    return res

def heappush(l, newnode):
    l.append(newnode)
    up(l, len(l)-1, cmp_lt)



class Solution:
    def mergeKLists(self, lists:list):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)
        i = 0
        while i<length:
            if lists[i] is None:
                lists.remove(None)
                length -= 1
            else:
                i += 1


        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        l = [None] + lists
        heapify(l)
        res = None
        p = None
        while len(l) > 1:
            if res is None:
                t = heappop(l)
                res = t
                p = res
                if t.next:
                    heappush(l, t.next)
            else:
                t = heappop(l)
                p.next = t
                p = p.next
                if t.next:
                    heappush(l, t.next)
        return res


a = [stringToListNode("[0,1,2]"),
     stringToListNode("[-10,-8,-5,-4]"),
     stringToListNode("[]"), 
     stringToListNode("[]"),
     stringToListNode("[-3]"),
     stringToListNode("[-10,-9,-6,-4,-3,-2,-2,-1,2]"),
     stringToListNode("[-9,-9,-2,-1,0,1]"),
     stringToListNode("[-9,-4,-3,-2,2,2,3,3,4]")
     ]

prettyPrintLinkedList(Solution().mergeKLists(a))