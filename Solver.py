import pyautogui
import cv2, numpy as np
from PIL import Image
import BoardSolver
topLeftLocation = pyautogui.locateCenterOnScreen("TopLeft.png")
bottomRightLocation = pyautogui.locateCenterOnScreen("BottomRight.png")
sudokuGrid = [[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]]

print("Puzzle Location: ",topLeftLocation,bottomRightLocation)
size = (300,350)
im = pyautogui.screenshot(imageFilename="my_screenshot.png",region=(topLeftLocation[0],topLeftLocation[1],bottomRightLocation[0]-topLeftLocation[0],bottomRightLocation[1]-topLeftLocation[1] + 10))
im2 = Image.open("my_screenshot.png")
im2.thumbnail(size,Image.ANTIALIAS)
im2.save("my_screenshot2.png","PNG")
imageList = ["1","2","3","4","5","6","7","8","9"]
img_rgb = cv2.imread("my_screenshot2.png")
for index, imageIndex in enumerate(imageList):
    # Reads in the images into CV2 objects
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(str(imageIndex) + ".png",0)

    #Gets the width and height of the template object?
    w,h = template.shape[::-1]
    print("Width - Height: " , w,h)
    #finds the images in the main image
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.825

    loc = np.where(res >= threshold)
    print(loc)
    print(loc[::-1])
    print(*loc[::-1])
    #Draws rectangle, using zip?
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb,pt,(pt[0] + w, pt[1] + h), (0,0,255), 2)
    #enumerating through the xvalues of the locations
    for i in range(9):
        for j in range(9):
            for k, location in enumerate(loc[1]):
                if((location >= 6 + (33*i) and location <= 37 + (33*i)) and (loc[0][k] >= 1 + (33*j) and loc[0][k] <= 32 + (33*j))):
                    sudokuGrid[j][i] = index + 1

print(sudokuGrid)
cv2.imshow("output",img_rgb)
cv2.waitKey(0)

#Start input onto webpage
solvedBoard = BoardSolver.solveBoard(sudokuGrid)
for i in range(9):
    try:
        firstIndex = [i,sudokuGrid[i].index(0)]
        break
    except:
        pass
print(firstIndex)
pyautogui.click((topLeftLocation[0] + 25 + (31 * firstIndex[1]),topLeftLocation[1] + 25 + (31 * firstIndex[0])))

for rowIndex, row in enumerate(sudokuGrid):
    for columnIndex, column in enumerate(row):
        if column != 0:
            if not(rowIndex == 8 and columnIndex == 8):
                pyautogui.press("tab")
        else:
            pyautogui.press(str(solvedBoard[rowIndex][columnIndex]))
            if not(rowIndex == 8 and columnIndex == 8):
                pyautogui.press("tab")
pyautogui.press("enter")
#Squares are 31 pixals long, starting at 6
#Sqaures are 31 pixals long, starting at 1