def calcScore(tosses):
    points = {'A': 1, 'R': 1, 'O': 3, 'G': 3, 'B': 6, 'AO': 5, 'OB': 10, 'BG': 10, 'GR': 5} # Dictionary for all points of all possible tosses
    tList = tosses.split() # Splits the tosses string into a list
    score = 0
    
    # Find the toss that matches with the dictionary term, gets the value of the toss, and adds it to score
    for toss in tList:
        score += points.get(toss, 0)
    
    return score # Return the score

def scoreTosses(tosses1, tosses2, tosses3):
    # Calculates the scores for each tosses by calling the function "calcScore"
    score1 = calcScore(tosses1)
    score2 = calcScore(tosses2)
    score3 = calcScore(tosses3)
    
    revScores = sorted([score1, score2, score3], reverse=True) # Reverses the scores
    
    return " ".join(map(str, revScores)) # Returns the numbers as a string with spaces between each number

print(scoreTosses("GR A B", "OB BG AO O", "R G")) # Should print out 28 12 4