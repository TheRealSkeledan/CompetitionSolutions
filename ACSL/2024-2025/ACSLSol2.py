import os
from collections import deque

def isValidCard(card1, card2):
    return sum(a == b for a, b in zip(card1, card2)) == 2

def printPile(piles, hand):
    pile1, pile2 = piles.split()
    hand = hand.split()
    
    piles = [deque([pile1]), deque([pile2])]
    maxPlayed = 0
    bestPile = 0
    finalPiles = [[], []]
    
    for i in range(2):
        tempPile = deque([piles[i][0]])
        tempHand = deque(hand)
        played = []
        
        while tempHand:
            for idx, card in enumerate(tempHand):
                if isValidCard(card, tempPile[-1]):
                    tempPile.append(card)
                    played.append(card)
                    tempHand.remove(card)
                    break
            else:
                break
        
        if len(played) > maxPlayed:
            maxPlayed = len(played)
            bestPile = i
            finalPiles[i] = list(tempPile)
    
    return " ".join(finalPiles[bestPile])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    piles = input()

    hand = input()

    result = printPile(piles, hand)

    fptr.write(result + '\n')

    fptr.close()
