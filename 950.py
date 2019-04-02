class Solution(object):
def deckRevealedIncreasing(self, deck):
    """
    :type deck: List[int]
    :rtype: List[int]
    """
    deck.sort()
    result = []
    for i in range(len(deck) - 1, -1, -1):
        if len(result)>0:
            result = [deck[i]] + [result[-1]] + result[:-1]
        else:
            result = [deck[i]]
    return result