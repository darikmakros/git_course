def getHatCats(numCats, numRounds):
    #INITIALIZE hats[numCats] to [False, False, ..., False] // массив длиной numCats
    hats = [False] * numCats
    #FOR roundNum in range(numRounds)
    for roundNum in range(numRounds):
        #FOR catNum in range(numCats)
        for catNum in range(numCats):
            #IF catNum is divisible by roundNum
            if catNum % roundNum == 0:
                #TOGGLE hats[catNum]
                hats[catNum] = not hats[catNum]
    #RETURN hats
    return hats

getHatCats(100, 100)