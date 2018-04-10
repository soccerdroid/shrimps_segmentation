from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import cv2

def cutSamples(coords_file, sample_name, photo, extension = "tiff", output_dir = ""):
	"""Cuts n samples from a photo, given coordinates and measures w (width) and h (height)"""
	file = open(coords_file,"r")
	file.readline()
	count = 1
	for line in file:
		x,y,w,h = line.strip().split(",")
		new_name = sample_name + str(count) + "." + extension
		im = Image.open(photo) #Can be many different formats.
		im.copy().crop((x,y,x+w,y+h)).save(output_dir+new_name)

def analysisRGB(file_name):

	im = Image.open(file_name) #Can be many different formats.
	
	f,col=im.size


	pix = im.load()


	num_pixeles=f*col
	r=np.zeros(num_pixeles)
	g=np.zeros(num_pixeles)
	b=np.zeros(num_pixeles)

	count=0
	for i in range(f):
		for j in range(col):
			pr,pg,pb=pix[i,j]
		
			r[count]=pr
			g[count]=pg
			b[count]=pb
			count+=1
	rgb = np.stack((r,g,b), axis=1)
	return rgb

def analysisHSV(file_name):
	# fig = plt.figure()
	# ax = fig.add_subplot(111, projection='3d')

	im = Image.open(file_name) #Can be many different formats.
	
	f,col=im.size


	pix = im.load()


	num_pixeles=f*col
	h=np.zeros(num_pixeles)
	s=np.zeros(num_pixeles)
	v=np.zeros(num_pixeles)

	count=0
	for i in range(f):
		for j in range(col):
			pr,pg,pb=pix[i,j]
			color=np.uint8([[[pr,pg,pb]]])
			color_hsv=cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
			h[count]=color_hsv[0][0][0]
			s[count]=color_hsv[0][0][1]
			v[count]=color_hsv[0][0][2]
			count+=1
	hsv = np.stack((h,s,v), axis=1)
	return hsv