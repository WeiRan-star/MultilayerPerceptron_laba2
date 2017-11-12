#this should return X and Y teaching sets.
from PIL import Image
import numpy


_TOTAL_FACES = 41
_TEACHING_PICS_PER_FACE = 8

#curfile = Image.open("faces/s1/1.pgm")


X = []
Xnorm = []
Y = []
Ynorm = []

def getListFromPGM(pgmf):
    currFile = Image.open(pgmf)
    shit = numpy.array(currFile)
    list2d = shit.tolist()
    finallist = []
    for i in range(len(list2d)):
        for j in range(len(list2d[0])):
            finallist.append(list2d[i][j])
    # print(list2d)
    # print(finallist)
    return(finallist)


def normalizeList(someList):
    resList = []
    for currX in range(len(someList)):
        resList.append(float(someList[currX]) / 255)
    outerList = []
    outerList.append(resList)
    return outerList

def getPGMAndNormalize(numF, numP):
    fileP = formFilePath(numF, numP)
    resulting = (normalizeList(getListFromPGM(fileP)))
    return resulting


#TODO: form the X/Y teachings sets from about a 7 images for each face.
def formFilePath(numFace, numImage):
    return "faces/s{0}/{1}.pgm".format(numFace, numImage)



def formTeachingArray():
    global X, Y
    for currFaceNum in range(1, _TOTAL_FACES):
        for currImgNum in range(1, _TEACHING_PICS_PER_FACE):
            currPath = formFilePath(currFaceNum, currImgNum)
            #curfile = Image.open(currPath)
            X.append(getListFromPGM(currPath))
            Y.append(currFaceNum)


def normalizeTeachingArray():
    for currX in range(len(X)):
        Xnorm.append([])
        Ynorm.append(float(Y[currX])/255)
        for currSubX in range(len(X[0])):
            Xnorm[currX].append(float(X[currX][currSubX]) / 255)


def glueTwoImages(f1, p1, f2, p2):
    image1 = Image.open(formFilePath(f1, p1))
    image2 = Image.open(formFilePath(f2, p2))
    w = image1.width
    h = image1.height
    gloodImg = Image.new("L", (w*2, h))
    gloodImg.paste(image1, (0,0))
    gloodImg.paste(image2, (w, 0))
    return gloodImg

    # complete bullshit:
# def read_pgm(pgmf):
#     #Return a raster of integers from a PGM as a list of lists.
#     assert pgmf.readline() == 'P5\n'
#     (width, height) = [int(i) for i in pgmf.readline().split()]
#     depth = int(pgmf.readline())
#     assert depth == 255
#
#     print("width={0}, height={1}, depth={2}".format(width, height, depth))
#
#     raster = []
#     schet = 0
#     for y in range(height):
#         row = []
#         for y in range(width):
#             schet+=1
#             currbyte = pgmf.read(1)
#             print(currbyte)
#             if currbyte == '':
#                 currbyte = chr(10)
#             row.append(ord(currbyte))
#         raster.append(row)
#     return raster