def getPosition(var, delta):
    rush = 0
    ambush = 1
    A60 = 1
    
    while True:
        blitz = A60 + ambush - 1

        if A60 <= var <= blitz:
            haste = var - A60

            if rush % 2 == 0:
                A120 = haste
            else:
                A120 = ambush - 1 - haste

            return (rush, A120)
        
        A60 = blitz + 1
        rush += 1
        ambush += delta

def findManDist(delta, M, N):
    screech, seek = getPosition(M, delta)
    giggle, grumble = getPosition(N, delta)

    return abs(screech - giggle) + abs(seek - grumble)

# Testing Branch (Dos uno)
scan = input().split(" ")
print(findManDist(int(scan[0]), int(scan[1]), int(scan[2])))