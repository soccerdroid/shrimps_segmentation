import cv2
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


# with open("coordenadas_paleta.txt") as f:
# 	for i, l in enumerate(f):
# 		pass
# 	lineas_paletas=i

# with open("coordenadas_camarones.txt") as f:
# 	for i, l in enumerate(f):
# 		pass
# 	lineas_camarones=i


ARCHIVO="matriz_datos.csv"
file=open(ARCHIVO,"a")
# file.write("etiqueta,fil,col,r,g,b,h,s,v,x,y,z\n")



# for i in range (lineas_paletas):
#   	nombre="paleta_cortada"+str(i+1)+".tiff"
#   	im = Image.open(nombre) #Can be many different formats.
# 	f,col=im.size
# 	pix = im.load()
# 	etiqueta="p2"+str(i)
# 	count=0
# 	for fi in range(f):
# 		for fj in range(col):
# 			pr,pg,pb=pix[fi,fj]
# 			color=np.uint8([[[pr,pg,pb]]])
# 			color_hsv=cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
# 			h=color_hsv[0][0][0]
# 			s=color_hsv[0][0][1]
# 			v=color_hsv[0][0][2]
# 			color_xyz=cv2.cvtColor(color,cv2.COLOR_BGR2XYZ)
# 			#print(color_xyz[0][0][2])
# 			x=color_xyz[0][0][0]
# 			y=color_xyz[0][0][1]
# 			z=color_xyz[0][0][2]
# 			linea=etiqueta+","+str(fi)+","+str(fj)+","+str(pr)+","+str(pg)+","+str(pb)+","+str(h)+","+str(s)+","+str(v)+","+str(x)+","+str(y)+","+str(z)+"\n"
# 			#etiqueta,fila,col,r,g,b,h,s,v,x,y,z
# 			#print(linea)
# 			file.write(linea)
				
  	

# for i in range (lineas_camarones):
#  	nombre="cortado"+str(i+1)+".tiff"
#  	im = Image.open(nombre) #Can be many different formats.
# 	f,col=im.size
# 	pix = im.load()
# 	etiqueta="c"+str(i)
# 	count=0
# 	for fi in range(f):
# 		for fj in range(col):
# 			pr,pg,pb=pix[fi,fj]
# 			color=np.uint8([[[pr,pg,pb]]])
# 			color_hsv=cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
# 			h=color_hsv[0][0][0]
# 			s=color_hsv[0][0][1]
# 			v=color_hsv[0][0][2]
# 			color_xyz=cv2.cvtColor(color,cv2.COLOR_BGR2XYZ)
# 			x=color_xyz[0][0][0]
# 			y=color_xyz[0][0][1]
# 			z=color_xyz[0][0][2]
# 			linea=etiqueta+","+str(fi)+","+str(fj)+","+str(pr)+","+str(pg)+","+str(pb)+","+str(h)+","+str(s)+","+str(v)+","+str(x)+","+str(y)+","+str(z)+"\n"
# 			#etiqueta,fila,col,y,r,g,b,h,s,v,x,y,z
# 			file.write(linea)
# 			#print(linea)

 	

referencia=open("ref_blanca_camarones.csv","r")
referencia.readline()
datos=referencia.readline().strip().split(",")
x=int(datos[0])
y=int(datos[1])
w=int(datos[2])
h=int(datos[3])

im = Image.open("0000000002.tiff") #Can be many different formats.
im.copy().crop((x,y,x+w,y+h)).save("ref_blanca_camarones.tiff")

im=Image.open("ref_blanca_camarones.tiff")
f,col=im.size
pix = im.load()

for fi in range(f):
	for fj in range(col):
		pr,pg,pb=pix[fi,fj]
		color=np.uint8([[[pr,pg,pb]]])
		color_hsv=cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
		h=color_hsv[0][0][0]
		s=color_hsv[0][0][1]
		v=color_hsv[0][0][2]
		color_xyz=cv2.cvtColor(color,cv2.COLOR_BGR2XYZ)
		x=color_xyz[0][0][0]
		y=color_xyz[0][0][1]
		z=color_xyz[0][0][2]
		etiqueta="rbc1"
		linea=etiqueta+","+str(fi)+","+str(fj)+","+str(pr)+","+str(pg)+","+str(pb)+","+str(h)+","+str(s)+","+str(v)+","+str(x)+","+str(y)+","+str(z)+"\n"
		#etiqueta,fila,col,y,r,g,b,h,s,v,x,y,z
		file.write(linea)


referencia=open("ref_blanca_paletas.csv","r")
referencia.readline()
datos=referencia.readline().strip().split(",")
x=int(datos[0])
y=int(datos[1])
w=int(datos[2])
h=int(datos[3])

im = Image.open("paleta.tiff") #Can be many different formats.
im.copy().crop((x,y,x+w,y+h)).save("ref_blanca_paletas.tiff")

im=Image.open("ref_blanca_paletas.tiff")
f,col=im.size
pix = im.load()


for fi in range(f):
	for fj in range(col):
		pr,pg,pb=pix[fi,fj]
		color=np.uint8([[[pr,pg,pb]]])
		color_hsv=cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
		h=color_hsv[0][0][0]
		s=color_hsv[0][0][1]
		v=color_hsv[0][0][2]
		color_xyz=cv2.cvtColor(color,cv2.COLOR_BGR2XYZ)
		x=color_xyz[0][0][0]
		y=color_xyz[0][0][1]
		z=color_xyz[0][0][2]
		etiqueta="rbp1"
		linea=etiqueta+","+str(fi)+","+str(fj)+","+str(pr)+","+str(pg)+","+str(pb)+","+str(h)+","+str(s)+","+str(v)+","+str(x)+","+str(y)+","+str(z)+"\n"
		#etiqueta,fila,col,y,r,g,b,h,s,v,x,y,z
		file.write(linea)
	





file.close()