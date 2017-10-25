boardList = [[[4], [2], [], [], [], [3], [8], [], []],
        [[], [], [3], [4], [], [], [2], [7], []],
        [[], [8], [], [], [2], [5], [9], [3], [4]],
        [[5], [], [1], [], [4], [], [], [], []],
        [[], [], [], [5], [], [7], [], [], []],
        [[], [], [], [], [6], [], [1], [], [3]],
        [[3], [1], [2], [8], [7], [], [], [4], []],
        [[], [5], [9], [], [], [4], [7], [], []],
        [[], [], [4], [9], [], [], [], [6], [1]]]

validAnswer = False

while validAnswer == False:
    for rowIndex, row in enumerate(boardList):
        for columnIndex, column in enumerate(row):
            if len(boardList[rowIndex][columnIndex]) == 0:
                #Add all possible values to array
                for x in range(9):
                    boardList[rowIndex][columnIndex].append(x + 1)

                if rowIndex > 2 and rowIndex < 6:
                    tempRowSearch = 3
                elif rowIndex > 5:
                    tempRowSearch = 6
                else:
                    tempRowSearch = 0
                if columnIndex > 2 and columnIndex < 6:
                    tempColumnSearch = 3
                elif rowIndex > 5:
                    tempColumnSearch = 6
                else:
                    tempColumnSearch = 0
                saveTemp = tempColumnSearch
                saveRowTemp = tempRowSearch
                # Box Search
                for tempRowSearch in range(tempRowSearch,tempRowSearch + 3):
                    tempColumnSearch = saveTemp
                    for tempColumnSearch in range(tempColumnSearch,tempColumnSearch + 3):
                        if len(boardList[tempRowSearch][tempColumnSearch]) != 1:
                            continue
                        elif boardList[tempRowSearch][tempColumnSearch][0] in boardList[rowIndex][columnIndex]:
                            boardList[rowIndex][columnIndex].remove(boardList[tempRowSearch][tempColumnSearch][0])

                #Column Search
                for tempColumnSearch in range(9):
                    if len(boardList[rowIndex][columnIndex]) == 1:
                        break
                    if len(boardList[rowIndex][tempColumnSearch]) != 1:
                        continue
                    elif boardList[rowIndex][tempColumnSearch][0] in boardList[rowIndex][columnIndex]:
                        boardList[rowIndex][columnIndex].remove(boardList[rowIndex][tempColumnSearch][0])
                #Row Search
                for tempRowSearch in range(9):
                    if len(boardList[rowIndex][columnIndex]) == 1:
                        break
                    if(len(boardList[tempRowSearch][columnIndex]) != 1):
                        continue
                    elif boardList[tempRowSearch][columnIndex][0] in boardList[rowIndex][columnIndex]:
                        boardList[rowIndex][columnIndex].remove(boardList[tempRowSearch][columnIndex][0])
                #Box Search for unique values
                tempRowSearch = saveRowTemp
                for tempRowSearch in range(tempRowSearch,tempRowSearch + 3):
                    tempColumnSearch = saveTemp
                    for tempColumnSearch in range(tempColumnSearch,tempColumnSearch + 3):
                        if len(boardList[tempRowSearch][tempColumnSearch]) > 1 and tempRowSearch != rowIndex and tempColumnSearch != columnIndex:
                              boardList[rowIndex][columnIndex] = list(set(boardList[rowIndex][columnIndex]) - set(boardList[tempRowSearch][tempColumnSearch]))
    possiblesCount = 0
    for row in boardList:
        for column in row:
            if len(column) != 1:
                possiblesCount += 1
    if possiblesCount == 0:
        validAnswer = True
    print(boardList)