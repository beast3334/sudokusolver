import copy
staticList = [[4, 2, 0, 0, 0, 3, 8, 0, 0],
        [0, 0, 3, 4, 0, 0, 2, 7, 0],
        [0, 8, 0, 0, 2, 5, 9, 3, 4],
        [5, 0, 1, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 1, 0, 3],
        [3, 1, 2, 8, 7, 0, 0, 4, 0],
        [0, 5, 9, 0, 0, 4, 7, 0, 0],
        [0, 0, 4, 9, 0, 0, 0, 6, 1]]

for i in range(9):
    try:
        firstIndex = [i,staticList[i].index(0)]
        break
    except:
        pass
print(firstIndex)
validEntry = False
activeList = copy.deepcopy(staticList)
activeIndex = list.copy(firstIndex)
activeSearch = 1
lastActiveIndex = list.copy(firstIndex)


def boxSearch(firstIndex,searchValue,boardList):
    if(firstIndex[0] >= 0 and firstIndex[0] < 4):
        rowSearchIndex = 0
    elif(firstIndex[0] > 3 and firstIndex[0] < 6):
        rowSearchIndex = 3
    else:
        rowSearchIndex = 6

    if(firstIndex[1] > 0 and firstIndex[1] < 4):
        columnSearchIndex = 0
    elif(firstIndex[1] > 3 and firstIndex[1] < 6):
        columnSearchIndex = 3
    else:
        columnSearchIndex = 6
    saveColumnIndex = columnSearchIndex
    for rowSearchIndex in range(rowSearchIndex,rowSearchIndex+3):
        columnSearchIndex = saveColumnIndex
        for columnSearchIndex in range(columnSearchIndex,columnSearchIndex+3):
            if boardList[rowSearchIndex][columnSearchIndex] == searchValue:
                return False
    return(True)
def columnSearch(firstIndex,searchValue,boardList):
    for i in range(9):
        if(boardList[firstIndex[0]][i] == searchValue):
            return False
    return True
def rowSearch(firstIndex,searchValue,boardList):
    for i in range(9):
        if boardList[i][firstIndex[1]] == searchValue:
            return False
    return True
def findEmptyIndex(boardList,currentPoint):
    foundIndex = False
    if currentPoint[1] == 9:
        currentPoint[0] -= 1
        currentPoint[1] = 0
    else:
        currentPoint[1] -= 1
    while not foundIndex:
        if boardList[currentPoint[0]][currentPoint[1]] != 0:
            if currentPoint[1] == 0:
                currentPoint[0] -= 1
                currentPoint[1] = 9
            else:
                currentPoint[1] -= 1
        else:
            return currentPoint
while validEntry == False:
    if(staticList[activeIndex[0]][activeIndex[1]] != 0):
        if activeIndex[1] == 9: #at the end of a row
            activeIndex[0] += 1
            activeIndex[1] = 0
        else:
            activeIndex[1] += 1
        continue
    if not boxSearch(activeIndex, activeSearch, activeList) or not columnSearch(activeIndex,activeSearch,activeList) or not rowSearch(activeIndex,activeSearch,activeList):
        if activeSearch == 9:
            activeIndex = findEmptyIndex(staticList,activeIndex)
            while activeList[activeIndex[0]][activeIndex[1]] == 9:
                activeIndex = findEmptyIndex(staticList,activeIndex)
            activeSearch = activeList[activeIndex[0]][activeIndex[1]] + 1
        else:
            activeSearch += 1
    else:
        activeList[activeIndex[0]][activeIndex[1]] = activeSearch
        activeSearch = 1
        if activeIndex[1] == 9:  # at the end of a row
            activeIndex[0] += 1
            activeIndex[1] = 0
        else:
            activeIndex[1] += 1
    print(activeList)