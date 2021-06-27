from collections import deque

def deckRevealedIncreasing(deck):
    result = deque([])
    deck.sort()
    while deck:
        poped = deck.pop()
        if len(result) != 0:
            ret_pop = result.pop()
            result.appendleft(ret_pop)
            result.appendleft(poped)
        else:
            result.append(poped)
    return list(result)

def solution(deck):
    sorted_deck = sorted(deck)
    deck_dict = dict()
    for i in range(len(deck)):
        deck_dict[deck[i]] = i
        
    sorted_idx = []
    
    while deck:
        if len(deck) > 1:
            card = deck.pop(0)
            sorted_idx.append(deck_dict[card])
            deck[:] = deck[1:] + deck[:1]
        else:
            sorted_idx.append(deck_dict[deck.pop()])
    
    result = [0] * len(sorted_deck)
    for i in sorted_idx:
        result[i] = sorted_deck.pop(0)
        
    return result






        


deck = [17,13,11,2,3,5,7]
print(solution(deck))

