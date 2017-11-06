#this should return X and Y teaching sets.
from PIL import Image
import numpy
pil_currentfile = Image.open("faces/s1/1.pgm")
cfile = open("faces/s1/1.pgm", 'r')


def read_pgm(pgmf):
    fuck = numpy.array(pgmf)
    print(fuck.tolist())


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