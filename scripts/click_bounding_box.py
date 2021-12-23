#%%

import cv2

points = []
img = cv2.imread("../data/img1.jpg")
drawing = False



def click_and_crop(event, x, y, flags, params):

    global points

    if event == cv2.EVENT_LBUTTONDOWN:
	    points = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP:

        points.append((x, y))
        # draw a rectangle around the region of interest
        cv2.rectangle(img, points[0], points[1], (0, 255, 0), 2)
        cv2.imshow("image", img)


clone = img.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)


while True:
	cv2.imshow("image", img)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break




cv2.destroyAllWindows()
cv2.waitKey(1)
# %%
