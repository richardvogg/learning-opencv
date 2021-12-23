#%%

import numpy as np
import cv2

with open('../data/results.txt') as f:
    lines = f.readlines()

frames = [int(item.split(",")[0]) for item in lines]



#%%
cap = cv2.VideoCapture("../data/VID_20210223_123630_0.mp4")

count = 1

while True:

    indices = [i for i, x in enumerate(frames) if x == count]

    dets = [lines[i] for i in indices]
    success, img = cap.read()
    
    for det in dets:
        dt = det.split(",")
        cv2.rectangle(img, (int(float(dt[2])), int(float(dt[3]))), 
        (int(float(dt[2]) + float(dt[4])), int(float(dt[3]) + float(dt[5]))),(255,0,0),4)
    
    cv2.imshow("test", img)

    key = cv2.waitKey(0)

    while key not in [ord('q'), ord('d')]:
        key = cv2.waitKey(0)

    count = count + 1

    if key == ord("q"):
        break

cv2.destroyAllWindows()
cv2.waitKey(1)

# %%
