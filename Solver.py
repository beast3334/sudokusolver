import pyautogui
import cv2, numpy as np
topLeftLocation = pyautogui.locateCenterOnScreen("TopLeft.png")
bottomRightLocation = pyautogui.locateCenterOnScreen("BottomRight.png")
print("Puzzle Location: ",topLeftLocation,bottomRightLocation)

im = pyautogui.screenshot(imageFilename="my_screenshot.png",region=(topLeftLocation[0],topLeftLocation[1],bottomRightLocation[0]-topLeftLocation[0],bottomRightLocation[1]-topLeftLocation[1]))

# Reads in the images into CV2 objects
img_rgb = cv2.imread("my_screenshot.png")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread("5.png",0)

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

cv2.imshow('output',img_rgb)
cv2.waitKey(0)


# method = cv2.TM_SQDIFF_NORMED
#
# small_image = cv2.imread('9.png')
# large_image = cv2.imread("my_screenshot.png")
#
# result = cv2.matchTemplate(small_image,large_image,method)
#
# mn,_,mnLoc,_ = cv2.minMaxLoc(result)
#
# MPx,MPy = mnLoc
#
# trows,tcols = small_image.shape[:2]
#
# cv2.rectangle(large_image,(MPx,MPy),(MPx + tcols,MPy + trows),(0,0,255),2)
# cv2.imshow('output',large_image)
# cv2.waitKey(0)
