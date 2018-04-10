
import cv2
import numpy as np
#from scipy import ndimage 
#img = cv2.imread('camaron_caja_negra.tiff',0)
img = cv2.imread('0000000002.tiff',0)

size = np.size(img)
skel = np.zeros(img.shape,np.uint8)

bilateral_filtered_image = cv2.bilateralFilter(img, 5, 35, 150)
ret,threshold = cv2.threshold(bilateral_filtered_image,24,255,0)

cv2.imshow("threshold",threshold)
cv2.waitKey(0)
cv2.imwrite("camarones_ocvthreshold_39.tiff",threshold)
cv2.destroyAllWindows()

element = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
done = False
count=0
while( not done):
    eroded = cv2.erode(threshold,element)
    temp = cv2.dilate(eroded,element)
    temp = cv2.subtract(threshold,temp)
    skel = cv2.bitwise_or(skel,temp)
    threshold = eroded.copy()
 
    zeros = size - cv2.countNonZero(threshold)
    
    if zeros==size:
        done = True
    count+=1
 
cv2.imshow("skel",skel)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("esqueletos_ocv_2.jpg",skel)
# labels,nblabels = ndimage.label(skel)
# plt.imshow(labels,'jet')
# plt.show()
# print(labels)