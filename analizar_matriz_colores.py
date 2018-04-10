from analisis_imagenes import analisis_camarones, analisis_camarones_simple
from analisis_camarones_hsv import analisis_camarones_hsv,analisis_camarones_hsv_raw
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from scipy.stats import zscore
#ax = fig.add_subplot(111, projection='3d')

#leer el archivo linea a linea
#cada etiqueta sera la clave de un diccionario
#esa clave tendra como valor otro diccionario
#el diccionario contendra como claves los canales r,g,b,h,s,v,x,y,z
#y como valores los valores en esos colores de los pixeles

#EJEMPLO
#{c1:{h:[],s:[],v:[] y asi sucesivamente...},c2:{},...}
def cargar_matriz_colores(archivo):
	dic_colores={}
	file=open(archivo,"r")
	file.readline()
	r=[]
	g=[]
	b=[]
	h=[]
	s=[]
	v=[]
	x=[]
	y=[]
	z=[]
	for line in file:
		datos=line.strip().split(",")
		etiqueta=datos[0]
		if etiqueta in dic_colores.keys():
			dic_colores[etiqueta]["r"].append(int(datos[3]))
			dic_colores[etiqueta]["g"].append(int(datos[4]))
			dic_colores[etiqueta]["b"].append(int(datos[5]))
			dic_colores[etiqueta]["h"].append(int(datos[6]))
			dic_colores[etiqueta]["s"].append(int(datos[7]))
			dic_colores[etiqueta]["v"].append(int(datos[8]))
			dic_colores[etiqueta]["x"].append(int(datos[9]))
			dic_colores[etiqueta]["y"].append(int(datos[10]))
			dic_colores[etiqueta]["z"].append(int(datos[11]))

		else:
			dic_canales={}
			dic_canales["r"]=[]
			dic_canales["g"]=[]
			dic_canales["b"]=[]
			dic_canales["h"]=[]
			dic_canales["s"]=[]
			dic_canales["v"]=[]
			dic_canales["x"]=[]
			dic_canales["y"]=[]
			dic_canales["z"]=[]

			dic_colores[etiqueta]=dic_canales

	file.close()
	return dic_colores

ARCHIVO="matriz_datos.csv"

df=pd.read_csv("matriz_datos.csv")
lista=["rbc1","rbp1","p20","p21","p22","p23","p24"]
lista2=["rbc1","rbp1","c0","c1","c2","c3","c4"]
lista3=["c0","c1","c2","c3","c4","p20","p21","p22","p23","p24"]

#promedio de r para la referencia de los camarones y paleta
mean_rbc=df.loc[df['etiqueta']=="rbc1", ['r']].mean()
mean_rbp=df.loc[df['etiqueta']=="rbp1", ['r']].mean()
#max_r=df.loc[~df.etiqueta.isin(lista3),"r"].max()
df.loc[~df.etiqueta.isin(lista),"r"]*=(1/float(mean_rbc))
df.loc[~df.etiqueta.isin(lista2),"r"]*=(1/float(mean_rbp))
#df.loc[~df.etiqueta.isin(lista3),"r"]*=(1/float(max_r))

#promedio de g para la referencia de los camarones y paleta
mean_rbc=df.loc[df['etiqueta']=="rbc1", ['g']].mean()
mean_rbp=df.loc[df['etiqueta']=="rbp1", ['g']].mean()
#max_g=df.loc[~df.etiqueta.isin(lista3),"g"].max()
df.loc[~df.etiqueta.isin(lista),"g"]*=(1/float(mean_rbc))
df.loc[~df.etiqueta.isin(lista2),"g"]*=(1/float(mean_rbp))
#df.loc[~df.etiqueta.isin(lista3),"g"]*=(1/float(max_g))



#promedio de b para la referencia de los camarones y paleta
mean_rbc=df.loc[df['etiqueta']=="rbc1", ['b']].mean()
mean_rbp=df.loc[df['etiqueta']=="rbp1", ['b']].mean()
#max_b=df.loc[~df.etiqueta.isin(lista3),"b"].max()
df.loc[~df.etiqueta.isin(lista),"b"]*=(1/float(mean_rbc))
df.loc[~df.etiqueta.isin(lista2),"b"]*=(1/float(mean_rbp))
#df.loc[~df.etiqueta.isin(lista3),"b"]*=(1/float(max_b))


#promedio de h para la referencia de los camarones y paleta
#mean_rbc=df.loc[df['etiqueta']=="rbc1", ['h']].mean()
#mean_rbp=df.loc[df['etiqueta']=="rbp1", ['h']].mean()
max_h=df.loc[df.etiqueta.isin(lista3),"h"].max()
#df.loc[~df.etiqueta.isin(lista),"h"]*=(1/float(mean_rbc))
#df.loc[~df.etiqueta.isin(lista2),"h"]*=(1/float(mean_rbp)) PROMEDIO ES CERO
df.loc[df.etiqueta.isin(lista3),"h"]*=(360/float(max_h))
 
#promedio de s para la referencia de los camarones y paleta
#mean_rbc=df.loc[df['etiqueta']=="rbc1", ['s']].mean()
#mean_rbp=df.loc[df['etiqueta']=="rbp1", ['s']].mean()
max_s=df.loc[df.etiqueta.isin(lista3),"s"].max()
#print(max_s)
#df.loc[~df.etiqueta.isin(lista),"s"]*=(1/float(mean_rbc))
#df.loc[~df.etiqueta.isin(lista2),"s"]*=(1/float(mean_rbp)) PROMEDIO ES CERO
df.loc[df.etiqueta.isin(lista3),"s"]*=(100/float(max_s))

#promedio de v para la referencia de los camarones y paleta
mean_rbc=df.loc[df['etiqueta']=="rbc1", ['v']].mean()
mean_rbp=df.loc[df['etiqueta']=="rbp1", ['v']].mean()
df.loc[~df.etiqueta.isin(lista),"v"]*=(1/float(mean_rbc))
df.loc[~df.etiqueta.isin(lista2),"v"]*=(1/float(mean_rbp))

#promedio de x para la referencia de los camarones y paleta
mean_rbc=df.loc[df['etiqueta']=="rbc1", ['x']].mean()
mean_rbp=df.loc[df['etiqueta']=="rbp1", ['x']].mean()
df.loc[~df.etiqueta.isin(lista),"x"]*=(1/float(mean_rbc))
df.loc[~df.etiqueta.isin(lista2),"x"]*=(1/float(mean_rbp))

#promedio de y para la referencia de los camarones y paleta
mean_rbc=df.loc[df['etiqueta']=="rbc1", ['y']].mean()
mean_rbp=df.loc[df['etiqueta']=="rbp1", ['y']].mean()
df.loc[~df.etiqueta.isin(lista),"y"]*=(1/float(mean_rbc))
df.loc[~df.etiqueta.isin(lista2),"y"]*=(1/float(mean_rbp))

#promedio de z para la referencia de los camarones y paleta
mean_rbc=df.loc[df['etiqueta']=="rbc1", ['z']].mean()
mean_rbp=df.loc[df['etiqueta']=="rbp1", ['z']].mean()
df.loc[~df.etiqueta.isin(lista),"z"]*=(1/float(mean_rbc))
df.loc[~df.etiqueta.isin(lista2),"z"]*=(1/float(mean_rbp))

colores=['g', 'r', 'c', 'm', 'y', 'k', 'w']
colores2=["#fcd2b0","#fbbc89","#faa662","#f99b4e","#f9903b"]
# ax = plt.gca()
#
# for i in range(10):
# 	mydata = df.loc[df['etiqueta']==lista3[i], ['g']].dropna(how="any")
# 	mydata2 = df.loc[df['etiqueta']==lista3[i], ['s']].dropna(how="any")
# 	if(i<5):
# 		ax.scatter(mydata.values, mydata2.values, c=colores[i], marker="+")
# 	else:
# 		ax.scatter(mydata.values, mydata2.values, c=colores2[i-5], marker="o")


# ax.set_xlabel('G')
# ax.set_ylabel('S')
# ax.set_xlim(0,255)
# ax.set_ylim(0,255)
# plt.show()
pd.options.mode.chained_assignment = None  # default='warn'
df_camararones=df[df['etiqueta'].isin(lista3[:5])]
df_paleta=df[df['etiqueta'].isin(lista3[5:])]
df_camararones['s'] = (df_camararones['s'] - df_camararones['s'].mean())/df_camararones['s'].std(ddof=0)

df_camararones['g'] = (df_camararones['g'] - df_camararones['s'].mean())/df_camararones['g'].std(ddof=0)
df_paleta['s'] = (df_paleta['s'] - df_paleta['s'].mean())/df_paleta['s'].std(ddof=0)
df_paleta['g'] = (df_paleta['g'] - df_paleta['g'].mean())/df_paleta['g'].std(ddof=0)

ax = plt.gca()
for i in range(10):
	if(i<5):
		mydata=df_camararones.loc[df_camararones["etiqueta"]==lista3[i],["g"]]
		mydata2=df_camararones.loc[df_camararones["etiqueta"]==lista3[i],["s"]]
		ax.scatter(mydata.values,mydata2.values , c=colores[i], marker="+")
	else:
		mydata=df_paleta.loc[df_paleta["etiqueta"]==lista3[i],["g"]]
		mydata2=df_paleta.loc[df_paleta["etiqueta"]==lista3[i],["s"]]
		ax.scatter(mydata.values,mydata2.values, c=colores2[i-5], marker="o")


ax.set_xlabel('G')
ax.set_ylabel('S')
#ax.set_xlim(0,255)
#ax.set_ylim(0,255)
plt.show()