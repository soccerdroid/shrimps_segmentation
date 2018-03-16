import sys
#sys.path.append('/home/belen/recientex/cvr/pruebaCacao/lib')
import os
import numpy as np
import cv2
from scipy import ndimage
from skimage.color import rgb2gray
from skimage import io, filter
from shutil import copyfile
from os.path import join
import matplotlib.pyplot as plt


def binarize_otsu(img):
	#threshold = filter.threshold_otsu(img)
	threshold = np.std(img)
	#print("asdfadsf " + str(threshold))
	img_copy = img.copy()
	img_copy[img_copy<threshold] = 0;
	img_copy[img_copy>threshold] = 1;
	return img_copy

def transformObjects(objects, fils, cols):
	t_objects = []
	for o in objects:
		slice1 = o[0]
		slice2 = o[1]
		fila_inicial = slice1.start - 20 if slice1.start - 20 >= 0 else 0 
		fila_final = slice1.stop + 20 if slice1.stop + 20 <= fils else fils
		col_inicial = slice2.start - 20 if slice2.start - 20 >= 0 else 0
		col_final = slice2.stop + 20 if slice2.stop + 20 <= cols else cols
		#t = (slice1.start,slice1.stop,slice2.start,slice2.stop) # (fila1,fila final, columna1, columna final) las filas y cols finales no se incluyen [)
		t = (fila_inicial,fila_final,col_inicial,col_final)
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

#Save detected objects
def saveObjects(boundingBoxes,input_img,output_dir):
	count=1
	img=io.imread(input_img)
	for p in boundingBoxes:
		x = p[0]
		x2 = p[1]
		y = p[2]
		y2 = p[3]
		area= (x2 - x)*(y2 - y)
		if(area>17000):
			crop_img = img[x:x2,y:y2]
			name= "new_object"+str(count)+".tiff"
			path = join(output_dir,name)
			io.imsave(path,crop_img)
			count+=1



#Get console parameters
args = sys.argv[1:]


input_img = args[0]
input_img = input_img.strip()
output_dir= args[1].strip()
#output_dir = args[1]

#Get image and binarize it
img = io.imread(input_img)
img_gray = rgb2gray(img)
fils,cols=np.shape(img_gray)
img=binarize_otsu(img_gray)

#Label pixels with values different from 0
label_img, num_labels = ndimage.label(input=img)

io.imshow(img)
plt.show()

#Find bounding boxes of the objects in the image
objects = ndimage.find_objects(label_img);

# se transforman los objectos
# a una estructura mas facil
objects = transformObjects(objects,fils,cols)
# se los ordena de acuerdo al area
objects = sorted(objects,compareObjects)
# los 7 objetos mas grandes son
# los bounding boxes de las pepas
#for o in objects:
	#print(o[1] - o[0])*(o[3] - o[2])
boundingBoxes = objects[0:7]

#save an image per each shrimp
saveObjects(boundingBoxes,input_img,output_dir)
