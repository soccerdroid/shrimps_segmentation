import sys
sys.path.append('/home_local/obayona/Downloads/pruebaCacao/lib')
import os
import numpy as np
import cv2
import tifffile as tiff
from skimage import filters
from scipy import ndimage
from shutil import copyfile
from os.path import join
from ImageWorker import *

# recibe la ruta de una carpeta experimento donde
# se capturaron 6 pepas de cacao
# El script detecta las 6 pepas y guarda una carpeta experimento
# para cada pepa



# binariza la imagen
def binayImage(img):
	threshold = filters.threshold_otsu(img)
	img_copy = img.copy()
	img_copy[img_copy<threshold] = 0;
	img_copy[img_copy>threshold] = 1;
	return img_copy


def compare(lf1,lf2):
	value1 = lf1[1]
	value2 = lf2[1]
	dif = value1 - value2
	if(dif==0):
		return 0
	if(dif < 0):
		return -1
	if(dif>0):
		return 1


def transformObjects(objects):
	t_objects = []
	for o in objects:
		slice1 = o[0]
		slice2 = o[1]
		t = (slice1.start,slice1.stop,slice2.start,slice2.stop)
		t_objects.append(t)
	return t_objects;


def compareObjects(o1,o2):
	area1 = (o1[1] - o1[0])*(o1[3] - o1[2])
	area2 = (o2[1] - o2[0])*(o2[3] - o2[2])
	if(area1==area2):
		return 0
	if(area1<area2):
		return 1
	if(area1>area2):
		return -1 


def copyImgs(origen_dir,final_dir,x,x2,y,y2):
	img_names = [i for i in os.listdir(origen_dir) if i.endswith(".tif")]
	for img_name in img_names:
		path = join(origen_dir,img_name);
		img = tiff.imread(path);
		crop_img = img[x:x2,y:y2];
		path = join(final_dir,img_name);
		tiff.imsave(path,crop_img);


		

def createCopys(input_dir,output_dir,x,x2,y,y2):
	folders = ["cuboNormalizado"]
	for f in folders:
		origen_dir = join(input_dir,f)
		final_dir = join(output_dir,f)
		os.mkdir(final_dir)
		copyImgs(origen_dir,final_dir,x,x2,y,y2);
	#se copia fotoThor
	path = join(input_dir,"fotoThor/output.tif");
	img = tiff.imread(path);
	crop_img = img[x:x2,y:y2];
	path = join(output_dir,"output.tif");
	tiff.imsave(path,crop_img);
	#se copia archivos de texto	
	src = join(input_dir,"Data_Experimento.txt");
	dst = join(output_dir,"Data_Experimento.txt");
	copyfile(src, dst)



#------------------------------------------------
# MAIN
args = sys.argv[1:]


input_dir = args[0]
input_dir = input_dir[:-1]
output_dir = args[1]


# se carga una imagen del cubo para removerle el fondo
img_ref_dir = join(input_dir,"cuboNormalizado/longitud888.38.tif")
img_ref = tiff.imread(img_ref_dir);
binary = binayImage(img_ref);

# se etiquetan los pixeles con valores diferentes de cero
label_img, num_labels = ndimage.label(input=binary)
# se encuentran los bounding boxes de los objetos
objects = ndimage.find_objects(label_img);
if (len(objects) < 6):
	# deben haber al menos 6 objetos en la imagen,
	# porque son 6 pepas
	print "Error irreparable"
	sys.exit()

# se transforman los objectos
# a una estructura mas facil
objects = transformObjects(objects)
# se los ordena de acuerdo al area
objects = sorted(objects,compareObjects)
# los 6 objetos mas grandes son
# los bounding boxes de las pepas
boundingBoxes = objects[0:6]


cont = 1

# se guarda una imagen por cada pepa
for p in boundingBoxes:
	x = p[0]
	x2 = p[1]
	y = p[2]
	y2 = p[3]
	nameFolder = input_dir + "_" + str(cont)
	nameFolder = join(output_dir,nameFolder)
	os.mkdir(nameFolder)
	cont = cont + 1
	createCopys(input_dir,nameFolder,x,x2,y,y2)

