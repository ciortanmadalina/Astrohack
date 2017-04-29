

def removeNegs(na):
    for i in range(len(na)):
        for j in range(len(na)):
            na[i][j] = max(0,na[i][j])

    return na

def normalizeInt(na):
    ma = np.amax(na)
    mi = np.amin(na)

    na = na * (ma - mi)
    return na


# In[90]:
def removePeakAtPosition(data, x, y, size):
    imagewidth = len(data)
    center = imagewidth/2

    threshold = 0.1 #definition of "black"
    exlusionRadiusSquared = (imagewidth/10)**2  # radius around the center where we don't remove anything
    for i in range(imagewidth):
        if (
                ( x-i >= 0 and data[x-i][y] < threshold) or
                ( x+i < imagewidth and data[x+i][y] < threshold ) or
                ( y -i >= 0 and data[x][y-i] < threshold ) or
                ( y +i < imagewidth and data[x][y+i] < threshold )
            ):
            circlesize = i
            break

    for i in range(x-circlesize, x+circlesize):
        for j in range(y-circlesize, y+circlesize):
            if ( i >= 0 and i < len(data[1]) and
                 i >= 0 and j < len(data[1]) and
                     (x-i)**2 + (y-j)**2 <= circlesize**2):
                # exlusion zone
                if ( (center-i)**2 + (center-j)**2 >= exlusionRadiusSquared ):
                    data[i][j] = -55

    return data


def findMaxima(na):
    width = len(na)
    center = int(width / 2)

    #find lum center
    peakfound = False
    moved = False
    px = center
    py = center
    while True:
        moved = False
        for i in range(-2, 2):
            for j in range(-2, 2):
                if (na[px + i][py + j] > na[px][py]):
                    px = px + i
                    py = py + j
                    moved = True
                    break
        if (moved == False):
            peakfound = True
            break

    if (peakfound == True):
        centerLum = na[px][py]

    starLumThreshold = centerLum * 0.7
    exlusionRadiusSquared = (width/10)**2


    for x in range(width):
        for y in range(width):
            # find the peak:
            if na[x][y] <= starLumThreshold:
                continue
            # found a place where there's a peak. Find it
            peakfound = False
            moved = False
            px = x
            py = y
            while True:
                moved = False
                for i in range(-2,2):
                    for j in range(-2,2):
                        if ( px+i < 1 or py+j < 1 or px+i >= width or py+j >= width):
                            continue

                        if (na[px + i][py + j] > na[px][py]):
                            px = px + i
                            py = py + j
                            moved = True
                            break
                if (moved == False):
                    peakfound = True
                    break

            if (peakfound == True):
                # remove that peak
                if ((center - px) ** 2 + (center - py) ** 2 > exlusionRadiusSquared):
                    na = removePeakAtPosition(na,px,py,max(abs(py-y),abs(px-x))+1)
#            print("found", (px, py), (x, y))

    return na

def cleanupImage(na):
    na = removeNegs(na)
    na = findMaxima(na)
    return na
