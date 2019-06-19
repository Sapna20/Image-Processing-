import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils
img = cv2.imread('2.png')
img1 = imutils.resize(img)
img2 = img1[0:256,0:256]

indices = np.where(img2==[100])
coordinates = zip(indices[0], indices[1])
print(coordinates)
for i in coordinates:
	img2[i[0], i[1]] = (0,0,0)
cv2.imshow('img2',img2)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()