#%%

import cv2
import numpy as np
import os
print(os.getcwd())

#%%

## Read image

img = cv2.imread("../data/img1.jpg")


print(img.shape)
img_resize = cv2.resize(img, (300, 200))
img_cropped = img[200:500, 0:200]

img_blur = cv2.GaussianBlur(img, (15,15), 0)
img_canny = cv2.Canny(img, 100, 100)

kernel5 = np.ones((5,5), np.uint8)
kernel3 = np.ones((3,3), np.uint8)

img_erode = cv2.erode(img_canny, kernel3, iterations=1)
img_dilated = cv2.dilate(img_erode, kernel5, iterations = 2)

cv2.imshow("Output", img_cropped)
cv2.imshow("Canny", img_canny)
cv2.imshow("Dilated", img_dilated)

cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.waitKey(1)


#%%

#Video
#cap = cv2.VideoCapture("../data/VID_20210223_123551.mp4")

#Webcam
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(30) & 0xFF ==ord("q"):
        break

cv2.destroyAllWindows()
cv2.waitKey(1)


# %%

