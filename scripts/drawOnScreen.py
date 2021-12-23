#%%

import cv2
import numpy as np

ColorList = [[0, 47, 191, 179, 90, 255]]

myColors = [[203,192,255]]

#for drawing points
myPoints = [] 

def drawPoints(myPoints, myColors):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 5, myColors[point[2]], cv2.FILLED)


def findColor(img, imgResult, ColorList):
    
    newPoints = []

    lower = np.array([ColorList[0][0:3]])
    upper = np.array([ColorList[0][3:6]])
    mask = cv2.inRange(img, lower, upper)

    cv2.imshow("mask", mask)

    x,y = getContours(mask, imgResult)

    if x != 0 and y != 0:
        newPoints.append([x,y,0])

    return newPoints
    # cv2.circle(imgResult, (x,y), 10, myColors[0], cv2.FILLED)



def getContours(img, imgResult):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            cv2.drawContours(imgResult, cnt, -1, myColors[0],2)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri, True)
            x,y,w,h = cv2.boundingRect(approx)

    return x + w//2, y


cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = findColor(img, imgResult, ColorList)
    if len(newPoints) > 0:
        for point in newPoints:
            myPoints.append(point)
    if len(myPoints) > 0:
        drawPoints(myPoints, myColors)
    cv2.imshow("Video", imgResult)
    

    if cv2.waitKey(30) & 0xFF ==ord("q"):
        break

cv2.destroyAllWindows()
cv2.waitKey(1)
# %%
