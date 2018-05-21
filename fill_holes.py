import sys
import cv2;
import numpy as np;
 
# Read image
args = sys.argv[1:]
input_img = args[0]
img = cv2.imread(input_img,0)
 
# Threshold.
# Set values equal to or above 220 to 0.
# Set values below 220 to 255.
 
bilateral_filtered_image = cv2.bilateralFilter(img, 7, 35, 150)
thresh =int(np.mean(bilateral_filtered_image))
th,im_th = cv2.threshold(bilateral_filtered_image,thresh,255,cv2.THRESH_BINARY)
 
# Copy the thresholded image.
im_floodfill = im_th.copy()
 
# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
 
# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255);
 
# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
 
# Combine the two images to get the foreground.
im_out = im_th | im_floodfill_inv
 
# Display images.
cv2.imshow("Thresholded Image", im_th)
cv2.imshow("Floodfilled Image", im_floodfill)
cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
cv2.imshow("Foreground", im_out)
cv2.waitKey(0)