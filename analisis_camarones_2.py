from analisis_imagenes import analisis_camarones, analisis_camarones_simple
from analisis_camarones_hsv import analisis_camarones_hsv,analisis_camarones_hsv_raw
import matplotlib.pyplot as plt

fig = plt.figure()
#ax = plt.gca()
ax = fig.add_subplot(111, projection='3d')

file=open("coordenadas_paleta.txt","r")
file.readline()

colores1=['g', 'r', 'c', 'm', 'y', 'k', 'w']
colores=["#fcd2b0","#fbbc89","#faa662","#f99b4e","#f9903b"]
markers=["*","s","o","D","^"]

foto="paleta.tiff"


count=1
for line in file:
	x,y,w,h=line.strip().split(",")
	nombre="paleta_cortada"+str(count)+".tiff"
	r,g,b=analisis_camarones(int(x),int(y),20,20,nombre,foto)
	h,s,v=analisis_camarones_hsv_raw(int(x),int(y),20,20,nombre,foto)
	#ax.scatter(h,s,v, c=colores[count-1], marker="o")
 	ax.scatter(r,g,b,c=colores[count-1],marker="o")

	# registro.write(r+",")
	# registro.write(g+",")
	# registro.write(b)
	# registro.write("\n")

	count+=1

file.close()

# file2=open("coordenadas_camarones.txt","r")
# file2.readline()

# foto="0000000002.tiff"
# count=1
# for line in file2:
# 	x,y,w,h=line.strip().split(",")
# 	nombre="cortado"+str(count)+".tiff"
# 	r,g,b=analisis_camarones(int(x),int(y),int(w),int(h),nombre,foto)
# 	ax.scatter(r,g,b,c="b",marker=markers[count-1])
# 	count+=1

# file2.close()


# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
# ax.set_xlim3d(0,255)
# ax.set_ylim3d(0,255)
# ax.set_zlim3d(0,255)
# plt.show()



# with open("coordenadas_paleta.txt") as f:
# 	for i, l in enumerate(f):
# 		pass
# 	lineas_paletas=i

with open("coordenadas_camarones.txt") as f:
	for i, l in enumerate(f):
		pass
	lineas_camarones=i

# f=open("valores_paleta_hsv.txt","w")
# f.write("h,s,v")

# for i in range (lineas_paletas):
#  	nombre="paleta_cortada"+str(i+1)+".tiff"
#  	h,s,v=analisis_camarones_hsv(nombre)
#  	r,g,b=analisis_camarones_simple(nombre)
#  	# for i in range(h.size):
#  	# 	f.write(str(h[i])+","+str(s[i])+","+str(v[i])+"\n")
#  	#ax.scatter(h,s,v, c=colores[i], marker="+")
#  	ax.scatter(g,s, c=colores[i], marker="+")

#f.close()


# f=open("valores_camarones_hsv.txt","w")
# f.write("h,s,v")

for i in range (lineas_camarones):
 	nombre="cortado"+str(i+1)+".tiff"
 	h,s,v=analisis_camarones_hsv(nombre)
 	r,g,b=analisis_camarones_simple(nombre)
 	# for i in range(h.size):
 	# 	f.write(str(h[i])+","+str(s[i])+","+str(v[i])+"\n")
 	#ax.scatter(h,s,v,c=colores1[i],marker="o")
 	ax.scatter(r,g,b,c=colores1[i],marker="o")
 	#ax.scatter(g,s, c=colores1[i], marker=markers[i])

#f.close()

ax.set_xlabel('R')

ax.set_ylabel('G')


ax.set_zlabel('B')
ax.set_xlim3d(0,255)
#ax.set_xlim(0,179)
#ax.set_xlim(0,255)


ax.set_ylim3d(0,255)
#ax.set_ylim(0,255)

ax.set_zlim3d(0,255)
plt.show()