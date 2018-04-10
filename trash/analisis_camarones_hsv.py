import cv2
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def analisis_camarones_hsv(nombre):
	# fig = plt.figure()
	# ax = fig.add_subplot(111, projection='3d')

	im = Image.open(nombre) #Can be many different formats.
	
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
	
	return h,s,v
	# ax.scatter(h, s, v, c="b", marker="o")
	# ax.set_xlabel('X Label')
	# ax.set_ylabel('Y Label')
	# ax.set_zlabel('Z Label')
	# ax.set_xlim3d(0,179)#range for hue
	# ax.set_ylim3d(0,255) #range for saturation
	# ax.set_zlim3d(0,255) #Range for value
	# plt.show()

def analisis_camarones_hsv_raw(x,y,w,h,nombre,foto):
	im = Image.open(foto) #Can be many different formats.
	#cortar imagen
	#im.copy().crop((x,y,w,h)).save("cortado.tiff")
	im.copy().crop((x,y,x+w,y+h)).save(nombre)
	im = Image.open(nombre) #Can be many different formats.
	
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
	
	return h,s,v

# def analisis_camarones(x,y,w,h,file_name,foto):

# 	im = Image.open(foto) #Can be many different formats.
# 	#cortar imagen
# 	#im.copy().crop((x,y,w,h)).save("cortado.tiff")
# 	im.copy().crop((x,y,x+w,y+h)).save(file_name)

# 	im=Image.open(file_name)

# 	#f,c=piece.size #Get the width and hight of the image for iterating over
# 	f,col=im.size


# 	pix = im.load()


# 	num_pixeles=f*col
# 	r=np.zeros(num_pixeles)
# 	g=np.zeros(num_pixeles)
# 	b=np.zeros(num_pixeles)

# 	count=0
# 	for i in range(f):
# 		for j in range(col):
# 			pr,pg,pb=pix[i,j]
		
# 			r[count]=pr
# 			g[count]=pg
# 			b[count]=pb
# 			count+=1
	
# 	return r,g,b