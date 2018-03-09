import os
import cv2 
import numpy as np




class CentroidsWorker(object):
	def __init__(self,objects_dir,extension="tiff"):
		super(CentroidsWorker,self).__init__()
		self.obejcts_dir=objects_dir
		self.extension=extension

	def setObjectsDir(self,objects_dir):
		"""Setter of objects directory"""
		self.objects_dir=objects_dir

	def setExtension(self,extension):
		"""Setter of extension"""
		self.extension=extension

	def calculateCentroid(self,image):
		"""This function calculates the centroid coordinates of a given images, returning a tuple"""
		im=cv2.imread(image,0) #reads it in greyscale
		ret,thresh = cv2.threshold(img_copy,128,255,cv2.THRESH_OTSU)
		im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
		cnt = contours[0]
		M = cv2.moments(cnt)
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
		centroid=(cx,cy)
		return centroid


	def getCentroids(self):
		"""This functions gets the coordinates of the centroids of each object detected inside an image.
		All the objects must be inside a folder, and there must be an image per each detected object.
		This functions is a complement of shrimps_cropper"""
		images=[]
		centroids_dict={}
		#Find all images of the objects
		for file in os.listdir(objects_dir):
	    	if file.endswith(self.extension):
	        	images.append(os.path.join(self.objects_dir, file))
	    #calculate centroid for every object and stores it in a dictionary
	    for image in images:
	    	centroid=calculateCentroid(image)
	    	centroids_dict[image]=centroid
	    return centroids_dict

	def centroidsToCsv(centroids_dict):
		"""This functions parses a dict with the centroid of objects to a csv)"""
		file=open("centroids.csv","w")
		file.write("image,cx,cy"+"\n")
		for k,v in centroids_dict:
			cx,cy=v
			cx,cy=int(cx),int(cy)
			line=k+","+str(cx)+","+str(cy)+"\n"
			file.write(line)
		file.close()

	
