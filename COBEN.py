## The number of points each athlete gets
points = [200, 180, 160, 140, 130, 120, 110, 100, 90, 80, 72, 64, 56, 48, 40, 36, 32, 28, 24, 20, 18, 16, 14, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -20]
## The number of trials to do
numRuns = 10000

import random

## You need to pass a list of points here
## For example, main([10, 5, 0])
def main(aList):
    ## Create elimination list
    elimList = []
    for i in range(len(aList)):
        elimList = elimList + [0]
    ## Cutoff points list if too many
    pointsShort = points[:len(aList)]
    ## Keep doing trials
    for i in range(numRuns):
        ## Randomly rank marbles
        random.shuffle(pointsShort)
        ## Make list
        tempList = []
        ## Sum points
        for i in range(len(aList)):
            tempList += [pointsShort[i] + aList[i]]
        ## find minimum
        minEle = min(tempList)
        for i in range(len(aList)):
            if (tempList[i] == minEle):
                elimList[i] += 1
    ## Return two-decimal string
    for i in range(len(elimList)):
        elimList[i] = elimList[i] / numRuns * 100
    return [ '%.2f' % elem + "%" for elem in elimList ]

## Just pass a multiplier here
## For example, pointMultiply(2) will double all scores
def pointMultiply(multiplier):
    for i in range(len(points)):
        points[i] *= multiplier
    print(points)

## Pass a list here
## Example: immune([10, 5, 0])
def immune(aList):
    ## Cutoff points list if too many
    pointsShort = points[:len(aList)]
    elimFound = False
    check = 0
    ## Sort list
    aList.sort()
    while (elimFound == False):
        tempList = []
        ## Sum points
        for i in range(len(aList)):
            tempList += [pointsShort[i] + aList[i]]
        ## find minimum
        minEle = min(tempList)
        if (minEle == tempList[len(tempList)-1]):
            elimFound = True
        else:
            check += 1
            ## Swap places to check next marble
            placeTemp = aList[-1]
            aList[-1] = aList[-1*(check+1)]
            aList[-1*(check+1)] = placeTemp
    return "There are " + str(check) + " immune contestants for the next race."
