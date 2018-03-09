import cv2
import numpy as np
import cv2.cv as cv
import sys

img = cv2.imread('0000000002.tiff',0)
#img = cv2.medianBlur(img,5)
#img = cv2.GaussianBlur(img, (5, 5), 0)
bilateral_filtered_image = cv2.bilateralFilter(img, 7, 35, 150)

#cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

output = cv2.imread('0000000002.tiff',0)
output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(bilateral_filtered_image,cv.CV_HOUGH_GRADIENT,1,100,param1=45,param2=44,minRadius=50)
if (circles is None):
	sys.exit()


for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(output,(i[0],i[1]),i[2],(0,255,0),4)
    # draw the center of the circle
    cv2.circle(output,(i[0],i[1]),2,(0,0,255),3)




cv2.imshow('detected circles',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("detected_circles_hough_bilateral.jpg",output)
