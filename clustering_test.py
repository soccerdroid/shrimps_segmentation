import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math
import sklearn.cluster as cluster
from sklearn.metrics import silhouette_samples, silhouette_score
import time
from analisis_imagenes import analysisRGB, analysisHSV
#from analisis_camarones_hsv import analisis_camarones_hsv,analisis_camarones_hsv_raw

colores=["#fcd2b0","#fbbc89","#faa662","#f99b4e","#f9903b"]

fig = plt.figure()
#ax = plt.gca()
ax = fig.add_subplot(111, projection='3d')
rgb_total = None

for count in range (1,6):
	#nombre="paleta_cortada"+str(count)+".tiff"
	nombre="cortado"+str(count)+".tiff"

	rgb=analysisRGB(nombre)
	if (count!=1):
		rgb_total = np.concatenate((rgb_total,rgb), axis=0)
	else:
		rgb_total = rgb
	hsv=analysisHSV(nombre)



#KMEANS
n_clusters = 5
kmeans = cluster.KMeans(n_clusters)  
kmeans.fit(rgb_total)  
ax.scatter(rgb_total[:,0],rgb_total[:,1],rgb_total[:,2], c=kmeans.labels_) 
plt.show() 