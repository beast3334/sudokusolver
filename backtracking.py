import copy
staticList = [[0, 0, 8, 6, 3, 2, 0, 0, 1],
              [0, 1, 0, 0, 4, 5, 0, 0, 7],
              [0, 0, 2, 0, 9, 1, 5, 0, 0],
              [6, 0, 0, 0, 7, 8, 0, 2, 0],
              [0, 0, 7, 0, 0, 0, 8, 0, 0],
              [0, 9, 0, 1, 2, 0, 0, 0, 5],
              [0, 0, 3, 5, 8, 0, 6, 0, 0],
              [5, 0, 0, 2, 1, 0, 0, 7, 0],
              [2, 0, 0, 9, 6, 4, 3, 0, 0]]


for i in range(9):
    try:
        firstIndex = [i,staticList[i].index(0)]
        break
    except:
        pass
validEntry = False
activeList = copy.deepcopy(staticList)
activeIndex = list.copy(firstIndex)
activeSearch = 1
lastActiveIndex = list.copy(firstIndex)


def boxSearch(firstIndex,searchValue,boardList):
    topLeftRow = 0
    topLeftColumn = 0

    #determines top left row and column of current index square
    if firstIndex[0] >= 0 and firstIndex[0] <= 2:
        topLeftRow = 0
    elif firstIndex[0] >= 3 and firstIndex[0] <= 5:
        topLeftRow = 3
    else:
        topLeftRow = 6
    if firstIndex[1] >= 0 and firstIndex[1] <= 2:
        topLeftColumn = 0
    elif firstIndex[1] >= 3 and firstIndex[1] <= 5:
        topLeftColumn = 3
    else:
        topLeftColumn = 6

    for i in range(3):
        for j in range(3):
            if boardList[topLeftRow][topLeftColumn + i] == searchValue:
                return False
    return(True)
def columnSearch(firstIndex,searchValue,boardList):
    for row in boardList:
        if row[firstIndex[1]] == searchValue:
            return False
    return True
def rowSearch(firstIndex,searchValue,boardList):
    for number in boardList[firstIndex[0]]:
        if number == searchValue:
            return False
    return True

def findEmptyIndex(staticList,currentPoint):
    foundIndex = False
    currentPoint = changeCurrentIndex(currentPoint,False)
    while not foundIndex:
        if staticList[currentPoint[0]][currentPoint[1]] != 0:
            currentPoint = changeCurrentIndex(currentPoint,False)
        else:
            return currentPoint

def changeCurrentIndex(currentPoint,isDown = True):
    if isDown:
        if currentPoint[1] == 8:
            currentPoint[0] += 1
            currentPoint[1] = 0
        else:
            currentPoint[1] += 1

    else:
        if currentPoint[1] == 0:
            currentPoint[0] -= 1
            currentPoint[1] = 8
        else:
            currentPoint[1] -= 1
    return(currentPoint)
while validEntry == False:
    #if the current cell is not zero, then go back one cell and continue until it is 0
    while staticList[activeIndex[0]][activeIndex[1]] != 0:
        activeIndex = changeCurrentIndex(activeIndex)
    #once we have a cell that was orginally empty, and can be changed
    #Search the activeIndex at the current search value and evaluate if it is valid on the board.
    if not(boxSearch(activeIndex,activeSearch,activeList)) or not(rowSearch(activeIndex,activeSearch,activeList)) or not((columnSearch(activeIndex,activeSearch,activeList))):
        #increase the search value if less than 9, and resets current index and goes back one
        if activeSearch == 9:
            activeList[activeIndex[0]][activeIndex[1]] = 0
            activeIndex = findEmptyIndex(staticList,activeIndex)
            while(activeList[activeIndex[0]][activeIndex[1]] == 9):
                activeList[activeIndex[0]][activeIndex[1]] = 0
                activeIndex = findEmptyIndex(staticList,activeIndex)
            activeSearch = activeList[activeIndex[0]][activeIndex[1]] + 1
        else:
            activeSearch += 1
    #Current search term works!
    else:
        activeList[activeIndex[0]][activeIndex[1]] = activeSearch
        activeIndex = changeCurrentIndex(activeIndex)
        activeSearch = 1

    invalid = False
    for row in activeList:
        for column in row:
            if column == 0:
                invalid = True
                break
        if invalid:
            break

    if not invalid:
        validEntry = True
    for each in activeList:
        print(each)
    print()