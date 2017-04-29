
import numpy as np
import os
from PIL import Image
from scipy.signal import argrelextrema
import scipy.ndimage.filters as filters
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt

inputDir = "C:/temp/Train/"

def preProcessImage(fileName):
    global inputdir
    csv = np.genfromtxt (inputDir + fileName, delimiter=",")
    #numpy.save(inputDir + "numpy/" + fileName + ".npy", csv)
    return csv


# In[52]:


def saveImage(numpyArray, filename):
    height = len(numpyArray)
    
    print(height)
    img = Image.new('RGB', (height, height))
    for x in range(height):
        for y in range(height):
            greyscale = int(255*float(numpyArray[x][y]))
            img.putpixel((x,y),(greyscale,greyscale,greyscale))

    img.save(inputDir + "/images/" + filename + ".png", "PNG")
    print(filename)


# In[62]:

def normalizeInt(numpyArray):
   ma = np.amax(numpyArray)
   mi = np.amin(numpyArray)
   
   na = numpyArray * ( ma-mi)
#    ma = np.max
   print(ma, mi)
   print(na)
   return na
   


# In[90]:

def findMaxima(na):

    width = len(na[1])
    center = int(width/2)
    centerLum = na[center][center]


    plt.imshow(na)

    for x in range(width):
        for y in range(width):
            # find the peak:
            uuu = 3
            
    neighborhood_size = 3
    data = na
    threshold = 10





    data_max = filters.maximum_filter(data, neighborhood_size)
    maxima = (data == data_max)
    data_min = filters.minimum_filter(data, neighborhood_size)
    diff = ((data_max - data_min) > threshold)
    maxima[diff == 0] = 0

    labeled, num_objects = ndimage.label(maxima)
    slices = ndimage.find_objects(labeled)
    x, y = [], []
    for dy,dx in slices:
        x_center = (dx.start + dx.stop - 1)/2
        x.append(x_center)
        y_center = (dy.start + dy.stop - 1)/2    
        y.append(y_center)

    plt.imshow(data)
    plt.imshow(na)
    plt.savefig(inputDir + "/images/" + filename + "2.png" , bbox_inches = 'tight')

    plt.autoscale(False)
    plt.plot(x,y, 'ro')

    


# In[92]:


    
imgcount = 0

for filename in os.listdir(inputDir):
    if filename.endswith(".csv"):
        imgcount = imgcount+1
        if imgcount<10:
            print(filename)
            img = preProcessImage(filename)
            findMaxima(img)
            plt.imshow(img)
            #img = normalizeInt(img)
            #saveImage(img, filename)
            #preProcessImage(filename)


# In[ ]:



