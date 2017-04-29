import numpy as np
import os
from PIL import Image
import math
import imagecleanup as xyz

inputDir = "C:/temp/Train/SmallTrainSet/"

def preProcessImage(fileName):
    global inputdir
    csv = np.genfromtxt(inputDir + fileName, delimiter=",")
    # numpy.save(inputDir + "numpy/" + fileName + ".npy", csv)
    return csv

def saveImage(na, filename):
    height = len(na)
    width = len(na[0])
    img = Image.new('RGB', (height, width))
    #img = Image.fromarray(na)

    maxval = xyz.findLumCenter(na)

    for x in range(height):
        for y in range(width):
            greyscale = int(255 * float(na[x][y]))
            greyscale = int((255.0/maxval) * (float(na[x][y])))

            color = (greyscale, greyscale, greyscale)

            if ( na[x][y] == -55):
                color=(255,0,0)
            img.putpixel((x, y), color)

    img.save(inputDir + "/images/" + filename + ".png", "PNG")
#    print(filename)


imgcount = 0
import time
st = time.time()

maximg = 500

#debugimg = "1237645941824356443-i.csv"

#img = preProcessImage(debugimg)

for filename in os.listdir(inputDir):
    if filename.endswith(".csv"):
        imgcount = imgcount + 1
        if imgcount < maximg:
            #print(filename)
            img = preProcessImage(filename)
            #saveImage(img, filename)

            xxxx = img.copy()

            clean = xyz.cleanupImage(xxxx)
            #img = normalizeInt(img)

            combined = np.concatenate((img, clean), axis=0)
            saveImage(combined, filename + "xx")


end = time.time()

print((end-st)/maximg)

# 0.07472427368164063 per img
# 0.03822218656539917 per csv load