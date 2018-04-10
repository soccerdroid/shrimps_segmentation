import tifffile as tiff
import sys
import matplotlib.pyplot as plt
from skimage import morphology, io
import numpy as np
from scipy import ndimage
from skimage.filters import threshold_li
from skimage.util import img_as_ubyte
from skimage.color import rgb2gray
import cv2
import numpy as np

dir_input = sys.argv[1]
n_operations = 1
size_selem = 9



img=img_as_ubyte(io.imread(dir_input,as_grey=True))


#img =  tiff.imread(dir_input)

thresh = threshold_li(img)
img_close = img > thresh
#img_close = img/img.max()#tranformar de (255,0) a (1,0)

# #Closing Morph Operation
# selem = morphology.square(size_selem)

# for i in range(n_operations):#aplica n_operations-operaciones de closing
# 	img_close = morphology.binary_closing(img_close,selem)

#Skelotenization
img_skeleton = morphology.skeletonize(img_close)
img_skeleton = np.uint8(255*img_skeleton)
cv2.imwrite("esqueletos_skimage_2.jpg",img_skeleton)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
fig, axes = plt.subplots(1,3,figsize=(12, 6))
axes[0].imshow(img, interpolation='nearest', cmap=plt.cm.gray)
axes[0].set_axis_off()
axes[1].imshow(img_close, interpolation='nearest', cmap=plt.cm.gray)
axes[1].set_axis_off()
axes[2].imshow(img_skeleton, interpolation='nearest', cmap=plt.cm.gray)
axes[2].set_axis_off()
plt.show()
# labels,nblabels = ndimage.label(img_skeleton)
# plt.imshow(labels,'jet')
# plt.show()