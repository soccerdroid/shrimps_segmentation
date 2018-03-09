import cv2
import numpy as np

img_shrimps=cv2.imread("threshold_24.tiff",0)
#img_shrimps=cv2.imread('../0000000002.tiff',0)
kernel = np.ones((5,5),np.uint8)
#dilation = cv2.dilate(img_shrimps,kernel,iterations = 1)
#cv2.imshow("asdfads",dilation)
#cv2.waitKey(0)

mask=cv2.imread("detected_circles_mask_3.tiff",0)
mask_inv=cv2.bitwise_not(mask)
img_inv=cv2.bitwise_not(img_shrimps)

#cv2.imwrite("detected_circles_mask_3_inv.tiff",mask_inv)

img2_fg = cv2.bitwise_and(img_shrimps,mask_inv)
#img2_fg = cv2.bitwise_xor(img2_fg,mask)
#img2_fg = cv2.bitwise_not(img2_fg)
cv2.imshow("bitwise_and with r/2 radius cut",img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("bitwise_and_half_r_threshold.jpg",img2_fg)