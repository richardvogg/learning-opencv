#%%

import cv2
import numpy as np

img = np.zeros((512,512,3))

img[100:200] = 255, 0, 0


cv2.line(img, (1,1), (img.shape[1], img.shape[0]), (50, 50, 200))
cv2.rectangle(img, (100, 100), (250, 50), (0, 0, 200), thickness = 2)
cv2.rectangle(img, (100, 100), (50, 250), (0, 0, 200), cv2.FILLED)
cv2.circle(img, (200, 200), 50, (100, 100, 0), 2)
cv2.putText(img, "Monkey1", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 100, 255))

cv2.imshow("Image", img)
cv2.waitKey(0)  

cv2.destroyAllWindows()
cv2.waitKey(1)


#%%
# Stack images horizontally (or vertically with vstack)

hor = np.hstack((img, img))

cv2.imshow("Image", hor)
cv2.waitKey(0)  

cv2.destroyAllWindows()
cv2.waitKey(1)
# %%
