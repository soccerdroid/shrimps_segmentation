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
  if(h+radius>=cols or k+radius>=rows):
    return -1
  xx_ext, yy_ext = circle(k,h,radius)#numpy array of coords x , and other array of coords y
  xx_int, yy_int = circle(k,h,radius/2) 

  #img[xx_ext, yy_ext] = 255
  rango=len(xx_ext)
  rango2 = len(xx_int)
  lineas=[]
  
  for i in range (rango):
    if(xx_ext[i]<=rows and yy_ext[i]<=cols):
      coords=get_line((k,h),(xx_ext[i],yy_ext[i])) # list of tuples of all points of a line
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


def get_line(start, end):
    """Bresenham's Line Algorithm
    Produces a list of tuples from start and end
 
    >>> points1 = get_line((0, 0), (3, 4))
    >>> points2 = get_line((3, 4), (0, 0))
    >>> assert(set(points1) == set(points2))
    >>> print points1
    [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
    >>> print points2
    [(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
    """
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
 
    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)
 
    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
 
    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1
 
    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1
 
    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    #points_y = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        #points_y.append(coord[1])

        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
 
    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
        #points_y.reverse()
    #points_x=np.asarray(points_x)
    #points=np.asarray(points)

    return points

