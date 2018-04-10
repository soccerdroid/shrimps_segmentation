import numpy as np
#from skimage.draw import line, circle_perimeter
#from skimage.io import imread, imshow
#import tifffile as tiff
#import matplotlib.pyplot as plt



def circle_segmentation(img,h,k,radius):
  """function that retrieves the point in the perimeter of a circle, and draws lines from the 
  center to each perimeter point"""
  #rr and cc are the x and y coordinates respectively of points in the circle perimeter
  rows,cols=img.shape
  if(h+radius>=cols or k+radius>=rows or h-radius<0 or k-radius<0):
    return -1
  xx_ext, yy_ext = circle(k,h,radius)#numpy array of coords x , and other array of coords y
  xx_int, yy_int = circle(k,h,radius/2) 

  #img[xx_ext, yy_ext] = 255
  rango=len(xx_ext)
  rango2 = len(xx_int)
  lineas=[]
  
  for i in range (rango):
    if(xx_ext[i]<=rows and yy_ext[i]<=cols):
      #coords=get_line((k,h),(xx_ext[i],yy_ext[i]))
      coords=list(bresenham(k,h,xx_ext[i],yy_ext[i])) # list of tuples of all points of a line
       # list of tuples of all points of a line
      """Check if point in internal circle belongs to line"""
      for j in range(rango2):
        internal_point=(xx_int[j],yy_int[j])
        try:
          index=coords.index(internal_point)
          coords=coords[index:]
          coords=np.asarray(coords)
          lineas.append(coords)
          xx_int=np.delete(xx_int,j)
          yy_int=np.delete(yy_int,j)
          rango2-=1
          break
        except ValueError:
          break

      #img[coords[:,0],coords[:,1]] = 0
      
  return lineas


def circle(x0, y0, radius):
  """Midpoint circle algorithm 
  https://en.wikipedia.org/wiki/Midpoint_circle_algorithm """
  f = 1 - radius
  ddf_x = 1
  ddf_y = -2 * radius
  x = 0
  y = radius
  coords_x=[]
  coords_y=[]
  coords_x.append(x0)
  coords_y.append(y0 + radius)
  coords_x.append(x0)
  coords_y.append(y0 - radius)

  coords_x.append(x0 + radius)
  coords_y.append(y0)

  coords_x.append(x0 - radius)
  coords_y.append(y0)


  while (x < y):
      if (f >= 0): 
          y -= 1
          ddf_y += 2
          f += ddf_y
      x += 1
      ddf_x += 2
      f += ddf_x    
      coords_x.append(x0 + x)
      coords_y.append(y0 + y)

      coords_x.append(x0 - x)
      coords_y.append(y0 + y)

      coords_x.append(x0 + x)
      coords_y.append(y0 - y)

      coords_x.append(x0 - x)
      coords_y.append(y0 - y)

      coords_x.append(x0 + y)
      coords_y.append(y0 + x)

      coords_x.append(x0 - y)
      coords_y.append(y0 + x)

      coords_x.append(x0 + y)
      coords_y.append(y0 - x)

      coords_x.append(x0 - y)
      coords_y.append(y0 - x)

  coords_x=np.asarray(coords_x)
  coords_y=np.asarray(coords_y)

  return coords_x, coords_y




def bresenham(x0, y0, x1, y1):
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
    Input coordinates should be integers.
    The result will contain both the start and the end point.
    Source https://github.com/encukou/bresenham/blob/master/bresenham.py
    """
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
      yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
      if D >= 0:
        y += 1
        D -= 2*dx
      D += 2*dy