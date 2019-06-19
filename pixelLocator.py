import cv2
import numpy as np
import imutils
img = cv2.imread('2.png')
img1 = imutils.resize(img)
img2 = img1[0:256,0:256]            #roi(region of interest) of image

indices = np.where(img2==[100])
coordinates = zip(indices[0], indices[1])    #coordinates is the list of tuples. Each tuple represents a coordinate in image
print(coordinates)
for i in coordinates:
	print(i)                      #displays coordinate of required pixel
	img2[i[0], i[1]] = (0,0,255)   #changes pixel to red
cv2.imshow('img2',img2)				#opens image window
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
