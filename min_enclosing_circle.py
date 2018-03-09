import cv2
import numpy as np
import imutils
 
img = cv2.imread('0000000002.tiff',0)
blurred = cv2.GaussianBlur(img, (5, 5), 0)
ret,thresh = cv2.threshold(blurred,22,255,0)

contours,hierarchy = cv2.findContours(thresh, 1, 2)
cv2.imshow('threshold',thresh)
cv2.waitKey(0)

cnt = contours
print cnt
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
print(radius)
cv2.circle(img,center,radius,(0,255,0),2)

cv2.imshow('detected circles',img)
cv2.waitKey(0)

