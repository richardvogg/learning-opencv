#%%

import cv2
import numpy as np


img = cv2.imread("../data/img1.jpg")
print(img.shape)

def empty(a):
    pass

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 640, 440)
cv2.createTrackbar("HueMin", "Trackbar", 0, 179,empty)
cv2.createTrackbar("HueMax", "Trackbar", 179, 179,empty)
cv2.createTrackbar("SatMin", "Trackbar", 0, 255,empty)
cv2.createTrackbar("SatMax", "Trackbar", 255, 255,empty)
cv2.createTrackbar("ValMin", "Trackbar", 0, 255,empty)
cv2.createTrackbar("ValMax", "Trackbar", 255, 255,empty)


cap = cv2.VideoCapture(0)



while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hmin = cv2.getTrackbarPos("HueMin", "Trackbar")
    hmax = cv2.getTrackbarPos("HueMax", "Trackbar")
    smin = cv2.getTrackbarPos("SatMin", "Trackbar")
    smax = cv2.getTrackbarPos("SatMax", "Trackbar")
    vmin = cv2.getTrackbarPos("ValMin", "Trackbar")
    vmax = cv2.getTrackbarPos("ValMax", "Trackbar")

    lower = np.array([hmin, smin, vmin])
    upper = np.array([hmax, smax, vmax])
    mask = cv2.inRange(img, lower, upper)

    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF ==ord("q"):
        print(lower, upper)
        break
        

cv2.destroyAllWindows()
cv2.waitKey(1)

# %%

