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
    csv = np.genfromtxt(inputDir + fileName, delimiter=",")
    # numpy.save(inputDir + "numpy/" + fileName + ".npy", csv)
    return csv


def gaussian(height, center_x, center_y, width_x, width_y):
    """Returns a gaussian function with the given parameters"""
    width_x = float(width_x)
    width_y = float(width_y)
    return lambda x,y: height*np.exp(
                -(((center_x-x)/width_x)**2+((center_y-y)/width_y)**2)/2)

def moments(data):
    """Returns (height, x, y, width_x, width_y)
    the gaussian parameters of a 2D distribution by calculating its
    moments """
    total = data.sum()
    X, Y = np.indices(data.shape)
    x = (X*data).sum()/total
    y = (Y*data).sum()/total
    col = data[:, int(y)]
    width_x = np.sqrt(np.abs((np.arange(col.size)-y)**2*col).sum()/col.sum())
    row = data[int(x), :]
    width_y = np.sqrt(np.abs((np.arange(row.size)-x)**2*row).sum()/row.sum())
    height = data.max()
    return height, x, y, width_x, width_y

def fitgaussian(data):
    """Returns (height, x, y, width_x, width_y)
    the gaussian parameters of a 2D distribution found by a fit"""
    params = moments(data)
    errorfunction = lambda p: np.ravel(gaussian(*p)(*np.indices(data.shape)) -
                                 data)
    p, success = optimize.leastsq(errorfunction, params)
    return p


def saveImage(numpyArray, filename):
    height = len(numpyArray)

    print(height)
    img = Image.new('RGB', (height, height))
    for x in range(height):
        for y in range(height):
            greyscale = int(255 * float(numpyArray[x][y]))
            color = (greyscale, greyscale, greyscale)

            if ( numpyArray[x][y] == -55):
                color=(255,0,0)

            img.putpixel((x, y), color)

    img.save(inputDir + "/images/" + filename + ".png", "PNG")
    print(filename)


# In[62]:

def normalizeInt(numpyArray):
    ma = np.amax(numpyArray)
    mi = np.amin(numpyArray)

    na = numpyArray * (ma - mi)
    #    ma = np.max
    print(ma, mi)
    print(na)
    return na


# In[90]:
def removePeakAtPosition(data, x, y, size):

    subdata = data[x-(size+1):x+(size+1)][y-(size+1):y+(size+1)]

    gf = fitgaussian(subdata)

    deltaValue = data[x][y] - data[x-size][y-size]

    for i in range(x-size, x+size):
        for j in range(y-size, y+size):
            if ( i > 0 and i < len(data[1]) and
                 i > 0 and j < len(data[1])):
                data[i][j] = -55

    return data


def findMaxima(na):
    width = len(na[1])
    center = int(width / 2)
    centerLum = na[center][center]

    plt.imshow(na)

    for x in range(width):
        for y in range(width):
            # find the peak:
            if na[x][y] < centerLum:
                continue
            # found a place where there's a peak. Find it
            peakfound = False
            moved = False
            px = x
            py = y
            while True:
                moved = False
                for i in range(3):
                    for j in range(3):
                        if (na[px + (i - 2)][py + (j - 2)] > na[px][py]):
                            px = px + (i - 2)
                            py = py + (j - 2)
                            moved = True
                            break
                if (moved == False):
                    peakfound = True
                    break

            if (peakfound == True):
                # remove that peak
                # fit a gaussian on it, compute the values, remove it from source
                uuu = 3
                na = removePeakAtPosition(na,px,py, max(abs(py-y),abs(px-x))+1)
            print("found", (px, py), (x, y))

    plt.imshow(na)
    return na


# In[92]:



imgcount = 0

for filename in os.listdir(inputDir):
    if filename.endswith(".csv"):
        imgcount = imgcount + 1
        if imgcount < 10:
            print(filename)
            img = preProcessImage(filename)
            img = findMaxima(img)
            plt.imshow(img)
            # img = normalizeInt(img)
            saveImage(img, filename + "xx")
            # preProcessImage(filename)


# In[ ]:



