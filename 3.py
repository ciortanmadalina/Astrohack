import cv2
import csv
import numpy
import pandas as pd
import os

import matplotlib.pyplot as plt


print('test')

#img = cv2.imread("1237645941824356443-i.csv.png",0)

filename = "hack/data/Sample_Data/SAMPLE/1237645941824356443-g.csv"
filename = "hack/data/Sample_Data/SAMPLE/1237645943978983579-g.csv"

def exploreImage(filename) :
    input = numpy.genfromtxt (filename, delimiter=",")
    print(input[0][0])
    print(input.shape)
    max=numpy.amax(input)
    min=numpy.amin(input)
    print('Min %s max $s'% min, max)
    flux = input.sum()
    lum_x = numpy.sum(input, axis=0)
    lum_y = numpy.sum(input, axis=1)

    numpy.save('numpy/test.out', input)
    x = range(0, input.shape[0])

    plt.plot(x, lum_x, label='lum x')
    plt.plot(x, lum_y, label='lum y')
    plt.show()

#exploreImage(filename)

df = pd.read_csv('hack/data/sample.csv',sep=';')
ids = df.SDSS_ID.values

gids = ['SAMPLE/'+str(id)+'-g.csv' for id in ids]
iids = ['SAMPLE/'+str(id)+'-i.csv' for id in ids]

for filename in os.listdir("hack/data/Sample_Data/SAMPLE/"):
    if filename.endswith(".csv"):
        file = numpy.genfromtxt("hack/data/Sample_Data/SAMPLE/" + filename, delimiter=",")
        numpy.save('numpy/' + filename, file)


