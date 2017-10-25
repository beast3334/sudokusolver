import pyautogui
import cv2, numpy as np
topLeftLocation = pyautogui.locateCenterOnScreen("TopLeft.png")
bottomRightLocation = pyautogui.locateCenterOnScreen("BottomRight.png")
sudokuGrid = [[[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]],
              [[],[],[],[],[],[],[],[],[]]]

print("Puzzle Location: ",topLeftLocation,bottomRightLocation)

im = pyautogui.screenshot(imageFilename="my_screenshot.png",region=(topLeftLocation[0],topLeftLocation[1],bottomRightLocation[0]-topLeftLocation[0],bottomRightLocation[1]-topLeftLocation[1] + 10))

imageList = ["1","2","3","4","5","6","7","8","9"]
img_rgb = cv2.imread("my_screenshot.png")
for index, imageIndex in enumerate(imageList):
    # Reads in the images into CV2 objects
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(str(imageIndex) + ".png",0)

    #Gets the width and height of the template object?
    w,h = template.shape[::-1]
    print("Width - Height: " , w,h)
    #finds the images in the main image
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8

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
                    sudokuGrid[j][i].append(index + 1)

print(sudokuGrid)
cv2.imshow("output",img_rgb)
cv2.waitKey(0)




#Squares are 31 pixals long, starting at 6
#Sqaures are 31 pixals long, starting at 1