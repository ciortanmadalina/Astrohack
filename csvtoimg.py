from PIL import Image
import csv


for filename in os.listdir("../AstrohackDataSource/Astrohack/Data/Sample_Data/SAMPLE/"):
    if filename.endswith(".csv"):
        convertImageToPng(filename)



def convertImageToPng(  fileName ):
    lines = []
    linecount = 0
    with open("../AstrohackDataSource/Astrohack/Data/Sample_Data/SAMPLE/1237645879578460255-i.csv", 'r') as csvfile:
        csvr = csv.reader(csvfile, delimiter = ',')
        for row in csvr:
            lines.append(row)
            linecount = linecount + 1

    print(lines[1])
    width = len(lines[1])

    #width = 300
    height = linecount
    img = Image.new('RGB', (width, height))
    for x in range(width):
        for y in range(height):
            greyscale = int(128+128*float(lines[x][y]))
            img.putpixel((x,y),(greyscale,greyscale,greyscale))

    img.save("1237645879578460255.png", "PNG")