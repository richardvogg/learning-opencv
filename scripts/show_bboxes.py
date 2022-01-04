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

        i = float(dt[1])
        c1 = float(dt[2])
        c2 = float(dt[3])
        c3 = float(dt[4])
        c4 = float(dt[5])

        color = (i * 100 % 255, i * 75 % 255, i * 50 % 255)

        cv2.rectangle(img, (int(c1), int(c2)), (int(c1 + c3), int(c2 + c4)), color, 4)
        cv2.rectangle(img, (int(c1),int(c2 + 30)), (int(c1 + 30),int(c2)), color, cv2.FILLED)
        cv2.putText(img, dt[1], (int(c1 + 5),int(c2 + 25)), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0))
    
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
