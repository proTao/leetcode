# Definition for singly-linked list.
import json

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# def stringToIntegerList(input):
#     return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def prettyPrintLinkedList(node, end=None):
    if end is None:
        while node and node.next:
            print(str(node.val) + "->", end='')
            node = node.next

        if node:
            print(node.val)
        else:
            print("Empty LinkedList")
    else:
        while node is not end:
            print(str(node.val) + "->", end='')
            node = node.next
        print(node.val)



if __name__ == "__main__":
    prettyPrintLinkedList(stringToListNode("[1,2,3]"))