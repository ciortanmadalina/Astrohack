import numpy as np
import os
from PIL import Image
import math
import imagecleanup as xyz

inputDir = "C:/temp/Train/"

def preProcessImage(fileName):
    global inputdir
    csv = np.genfromtxt(inputDir + fileName, delimiter=",")
    # numpy.save(inputDir + "numpy/" + fileName + ".npy", csv)
    return csv





def saveImage(na, filename):
    height = len(na)

    img = Image.new('RGB', (height, height))
    #img = Image.fromarray(na)
    for x in range(height):
        for y in range(height):
            greyscale = int(255 * float(na[x][y]))
            color = (greyscale, greyscale, greyscale)

            if ( na[x][y] == -55):
                color=(255,0,0)
            img.putpixel((x, y), color)

    img.save(inputDir + "/images/" + filename + ".png", "PNG")
#    print(filename)


imgcount = 0
import time
st = time.time()

maximg = 300

for filename in os.listdir(inputDir):
    if filename.endswith(".csv"):
        imgcount = imgcount + 1
        if imgcount < maximg:
            #print(filename)
            img = preProcessImage(filename)
            #saveImage(img, filename)

            img = xyz.cleanupImage(img)
            #img = normalizeInt(img)
            saveImage(img, filename + "xx")


end = time.time()

print((end-st)/maximg)

# 0.07472427368164063 per img
# 0.03822218656539917 per csv load