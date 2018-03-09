import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import bresenham


"""Open image in grayscale, apply bilateral filter and detect contours"""
img = cv2.imread('../0000000002.tiff',0)
#img = cv2.imread('../camaron_caja_negra.tif',0)
rows,cols=img.shape

#Threshold image
bilateral_filtered_image = cv2.bilateralFilter(img, 7, 35, 150)
ret,binary = cv2.threshold(bilateral_filtered_image,24,255,cv2.THRESH_BINARY)
mask=np.zeros(img.shape)


#Detected contours with cany, same output with just the binary image
#edge_detected_image = cv2.Canny(binary, 75, 200)
# cv2.imshow('Edge', edge_detected_image)
# cv2.waitKey(0)
#cv2.imwrite("edges.jpg",edge_detected_image)

#Find contours of shrimps 
contours= cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
contour_list = []
color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

for contour in contours:
    #approximate contours to a polygon 
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    area = cv2.contourArea(contour)
    #just look for big objects
    if ((len(approx) > 8) & (area > 50) ):
        contour_list.append(contour)
        #Draw minimun enclosing circle
        (x,y),radius = cv2.minEnclosingCircle(contour)
    	center = (int(x),int(y))
    	radius = int(radius)
        #if circles are inside the image
    	if(center[0]<=rows and center[1]<=cols):
    		#cv2.circle(img,center,radius,(255,255,255),2) #last parameter is thickness
            count=0
            #get segments of the ring delimitates by the external and internal circle that encloses the shrimps
            lineas=bresenham.circle_segmentation(img, center[0], center[1], radius)
            if(lineas!=-1):
            	desviaciones=[]
            	promedios=[]
                for linea in lineas:
                    #get intensities from the coordinates of the segments
                    intensidades=img[linea[:,0],linea[:,1]]
                    #plt.hist(intensidades.flatten(),256,[0,256], color = 'r')
                    #plt.xlim([0,256])
                    #plt.show()
                    #get standard deviation
                    std=np.std(intensidades)
                    mean=np.mean(intensidades)
                    if(std>35 or std<22):
                    #if(mean>100 or mean<70):
                        del lineas[count]
                    print(str(linea[0,0])+" , "+str(linea[-1,-1])+" -> "+str(std))
                    desviaciones.append(std)
                    count+=1
                for linea in lineas:
                    img[linea[:,0],linea[:,1]]=0
                desviaciones=np.asarray(desviaciones)
                ejex=np.arange(1,count+1)
    		  	plt.scatter(ejex, desviaciones)
    		  	plt.show()
            #cv2.circle(mask,center,radius/2,(0,255,255),-1)
    		



#cv2.drawContours(color_img, contour_list,  -1, (0,255,0), 2)
cv2.imshow('Objects Detected',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("detected_edges_and_circles_color.jpg",color_img)
#cv2.imwrite("mask.tiff",mask)