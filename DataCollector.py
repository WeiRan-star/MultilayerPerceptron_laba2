#this should return X and Y teaching sets.
from PIL import Image
import numpy

curfile = Image.open("faces/s1/1.pgm")


def getListFromPGM(pgmf):
    shit = numpy.array(pgmf)
    list2d = shit.tolist()
    finallist = []
    for i in range(len(list2d)):
        for j in range(len(list2d[0])):
            finallist.append(list2d[i][j])
    # print(list2d)
    # print(finallist)
    return(finallist)

#TODO: form the X/Y teachings sets from about a 7 images for each face.

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