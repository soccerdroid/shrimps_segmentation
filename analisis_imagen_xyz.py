import cv2
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from analisis_imagenes import analisis_camarones, analisis_camarones_simple
import pandas as pd
from scipy.stats import zscore
#MAX RANGE OF XYZ IS X=242,Y=255,Z=255

def analisis_imagen_xyz_completo(nombre):

	im = Image.open(nombre) 
	
	f,col=im.size

	pix = im.load()

	num_pixeles=f*col
	x=np.zeros(num_pixeles)
	y=np.zeros(num_pixeles)
	z=np.zeros(num_pixeles)

	count=0
	for i in range(f):
		for j in range(col):
			pr,pg,pb=pix[i,j]
			color=np.uint8([[[pr,pg,pb]]])
			color_xyz=cv2.cvtColor(color,cv2.COLOR_BGR2XYZ)
			x[count]=color_xyz[0][0][0]
			y[count]=color_xyz[0][0][1]
			z[count]=color_xyz[0][0][2]
			count+=1
	
	return x,y,z
	
def cortar_imagen(foto,x,y,w,h,nombre):
	im = Image.open(foto) 
	
	im.copy().crop((x,y,x+w,y+h)).save(nombre)



ARCHIVO="matriz_datos.csv"

df=pd.read_csv("matriz_datos.csv")
lista=["rbc1","rbp1","p20","p21","p22","p23","p24"]
lista2=["rbc1","rbp1","c0","c1","c2","c3","c4"]
lista3=["c0","c1","c2","c3","c4","p20","p21","p22","p23","p24"]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
colores=['g', 'r', 'c', 'm', 'y', 'k', 'w']
colores2=["#fcd2b0","#fbbc89","#faa662","#f99b4e","#f9903b"]
markers=["*","s","o","D","^"]


# for i in range(10):
# 	mydata = df.loc[df['etiqueta']==lista3[i], ['x']].dropna(how="any")
# 	mydata2 = df.loc[df['etiqueta']==lista3[i], ['y']].dropna(how="any")
# 	mydata3 = df.loc[df['etiqueta']==lista3[i], ['z']].dropna(how="any")

# 	if(i<5):
# 		ax.scatter(mydata.values, mydata2.values,mydata3.values, c=colores[i], marker="+")
# 	else:
# 		ax.scatter(mydata.values, mydata2.values,mydata3.values, c=colores2[i-5], marker="o")
# ax.set_zlabel('Z')
# ax.set_xlabel('Y')
# ax.set_ylabel('X')
# ax.set_xlim3d(0,242)
# ax.set_ylim3d(0,255)
# ax.set_zlim3d(0,255)
# plt.show()

#NORMALIZAR VALORES DIVIDIENDO PARA EL MAXIMO DE CADA CANAL

#NORMALIZAR X
x_max=df['x'].max()
df.loc[df.etiqueta.isin(lista3),"x"]*=(1/float(x_max))


#NORMALIZAR Y
y_max=df['y'].max()
df.loc[df.etiqueta.isin(lista3),"y"]*=(1/float(y_max))
#NORMALIZAR Z
z_max=df['z'].max()
df.loc[df.etiqueta.isin(lista3),"z"]*=(1/float(z_max))

# ax = plt.gca()
# for i in range(10):
# 	if(i<5):
# 		mydata=df_camararones.loc[df_camararones["etiqueta"]==lista3[i],["g"]]
# 		mydata2=df_camararones.loc[df_camararones["etiqueta"]==lista3[i],["s"]]
# 		ax.scatter(mydata.values,mydata2.values , c=colores[i], marker="+")
# 	else:
# 		mydata=df_paleta.loc[df_paleta["etiqueta"]==lista3[i],["g"]]
# 		mydata2=df_paleta.loc[df_paleta["etiqueta"]==lista3[i],["s"]]
# 		ax.scatter(mydata.values,mydata2.values, c=colores2[i-5], marker="o")


# ax.set_xlabel('G')
# ax.set_ylabel('S')
# ax.set_xlim(0,255)
# ax.set_ylim(0,255)
# plt.show()
for i in range(10):
	mydata = df.loc[df['etiqueta']==lista3[i], ['x']].dropna(how="any")
	mydata2 = df.loc[df['etiqueta']==lista3[i], ['y']].dropna(how="any")
	mydata3 = df.loc[df['etiqueta']==lista3[i], ['z']].dropna(how="any")
	print(mydata.values)
	if(i<5):
		ax.scatter(mydata.values, mydata2.values,mydata3.values, c=colores[i], marker="+")
	else:
		ax.scatter(mydata.values, mydata2.values,mydata3.values, c=colores2[i-5], marker="o")
ax.set_zlabel('Z')
ax.set_xlabel('Y')
ax.set_ylabel('X')
# ax.set_xlim3d(0,1)
# ax.set_ylim3d(0,1)
# ax.set_zlim3d(0,1)
plt.show()
