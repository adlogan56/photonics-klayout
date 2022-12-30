import pya
import csv

scale = 20  #pixels per nanometer

layout = pya.Layout()
layout.dbu = 0.001/scale
layer = layout.layer(1,0)

top = layout.create_cell("top")
origin = pya.Point(0,0)

negative = False;

size_px_x = round(12.5*scale) #in nanometers
size_px_y = round(12.5*scale)
enlarge = 0*scale  #extra size of pixel in nanometers

filename = "C:\\Users\\adlogan\\Dropbox\\Frequency Conversion\\Data\\KLayout\\Other\\Extractor\\extractor.csv"
savefile = "C:\\Users\\adlogan\\Dropbox\\Frequency Conversion\\Data\\KLayout\\Other\\Extractor\\extractor.gds"

#pixel = pya.Shape()
pixel = pya.Polygon(pya.Box(0,0,size_px_x+enlarge,size_px_y+enlarge))

empty_value = 0

with open(filename, 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  
  rownum = 0
  pixels = set()
  #pixels = layout.create_cell('pixels')


  for row in reader:
    rownum += 1
    length = len(row)
    for colnum in range(len(row)):
      if (negative ^ (float(row[colnum])!=empty_value)):
        tf = pya.Trans(pya.Point(colnum*size_px_x, -rownum*size_px_y))
        #pixels.shapes(layer).insert(tf.trans(pixel))
        pixels.add(tf.trans(pixel))
      

pr = pya.EdgeProcessor()

full_shape = pr.boolean_p2p(list(pixels),list(pixels),pya.EdgeProcessor.ModeOr,False,True)

if negative:
  holes = full_shape
  region = pya.Polygon(pya.Box(0,-rownum*size_px_x,length*size_px_y,0))
  full_shape = pr.boolean_p2p([region],holes,pya.EdgeProcessor.ModeANotB,False,True)


for shape in full_shape:
  top.shapes(layer).insert(shape)

#trans_center = pya.Trans(0,round(rownum*size_px_y/2))
#trans_45 = pya.ICplxTrans(1,45,False,0,0)
# 
#for shape in full_shape:
#  top.shapes(layer).insert(trans_45*trans_center*shape)
  
top.write(savefile) 



  