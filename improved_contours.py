import cv2
import numpy as np
import matplotlib.pyplot as plt
import bresenham
import sys
from os import listdir
from os.path import isfile, join

"""Get samples of every image of shrimps"""



def binarizeImage(img):
    bilateral_filtered_image = cv2.bilateralFilter(img, 7, 35, 150)
    thresh = int(np.std(bilateral_filtered_image))
    ret,binary = cv2.threshold(bilateral_filtered_image,thresh,255,cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    return binary

def isGoodSegment(img, segment):
    intensities = img[segment[:,0],segment[:,1]]
    std = np.std(intensities)
    mean = np.mean(intensities)
    #if(mean>100 or mean<70):
    return True if std<35 and std>22 else False

def extractSample(img, centerx, centery, radius):
    lines = bresenham.circle_segmentation(img, centerx, centery, radius)
    if(lineas!=-1):
        number_of_lines = len (lineas)
        for i in range number_of_lines:
            if not isGoodSegment(lines[i]):
                del lines[i]
    return lines




            


#MAIN


#Get console parameters
args = sys.argv[1:]
objects_dir = args[0].strip()

#Open every object image in output folder
onlyfiles = [f for f in listdir(objects_dir) if isfile(join(objects_dir, f))]

for img in onlyfiles:    
    #get binarized img
    binary = binarizeImage(img)
    rows,cols = img.shape
    #multiply original image with binarized image
    multiplication = np.multiply(binary,img)
    binary =  cv2.cvtColor(multiplication, cv2.COLOR_BGR2GRAY)
    #result in grayscale, in order to get segments from the multiplied img
    
    #detect contours
    contours = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contour_list = []
    for contour in contours:
        #approximate contours to a polygon 
        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        area = cv2.contourArea(contour)
        #just look for big objects
        if ((len(approx) > 10) & (area > 100) ):
            contour_list.append(contour)
            #detect circles
            (x,y),radius = cv2.minEnclosingCircle(contour)
            center = (int(x),int(y))
            radius = int(radius)
            #if circles are not inside the image
            if (center[0]>rows or center[1]>cols):
                print ("Detected circle exceeds size of image.Aborting...")
                sys.exit()
            count = 0
            #from circles, draw segments
            lines = extractSample(img,center[0], center[1], radius)
            #choose best segments, and slice those pixels with value 0

