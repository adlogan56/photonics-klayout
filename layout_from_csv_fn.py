import pya
import csv
import math


def inverse_design_v1(angle, delta_w, delta_L, enlarge, scale, diagonal=True):
  negative = (enlarge < 0);
  
  print(negative)
  
  size_px_x = round(31*scale*(1 + delta_L/(6200*scale))) #in nanometers
  size_px_y = round(31*scale*(1 + delta_w/(4250*scale)))
  
  filename = "C:\\Users\\adlogan\\Dropbox\\Frequency Conversion\\Data\\KLayout\\DFG250\\Inverse Design\\resonator_2019_01_27.csv"
  #pixel = pya.Shape()
  pixel = pya.Polygon(pya.Box(0,0,size_px_x+abs(enlarge),size_px_y+abs(enlarge)))
  
  
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    rownum = 0
    pixels = set()
    #pixels = layout.create_cell('pixels')
    all_pixels = set()
  
    for row in reader:
      rownum += 1
      length = len(row)
      for colnum in range(len(row)):
        tf = pya.Trans(pya.Point(colnum*size_px_x, -rownum*size_px_y))
        all_pixels.add(tf.trans(pixel))
        if (negative ^ (float(row[colnum])!=1)):
          #pixels.shapes(layer).insert(tf.trans(pixel))
          pixels.add(tf.trans(pixel))
        
  
  pr = pya.EdgeProcessor()
  
  full_shape = pr.boolean_p2p(list(pixels),list(pixels),pya.EdgeProcessor.ModeOr,False,True)
  
  if negative:
    holes = full_shape
    region = pr.boolean_p2p(list(all_pixels),list(all_pixels),pya.EdgeProcessor.ModeOr,False,True)
    full_shape = pr.boolean_p2p(region,holes,pya.EdgeProcessor.ModeANotB,False,True)
  
   
  trans_center = pya.Trans(0,round(rownum*size_px_y/2))
  trans_45 = pya.ICplxTrans(1,90+angle,False,0,0)
  
  if diagonal:
    trans_center = trans_45*trans_center
  
  shapes = set()
  for s in full_shape:
    shapes.add(trans_center*s)
  
  return (shapes,)
  

def inverse_design_v2(angle, delta_w, delta_L, enlarge, scale, diagonal=True, thickness=200):
  negative = (enlarge < 0);
  
  print(negative)
  
  size_px_x = round(31*scale*(1 + delta_L/(6200*scale))) #in nanometers
  size_px_y = round(31*scale*(1 + delta_w/(4250*scale)))
  
  if thickness == 250:
    filename = "C:\\Users\\adlogan\\Dropbox\\Projects\\Frequency Conversion\\Layout\\KLayout\\Inverse Design\\GaPOx250_shg2_2021_04_14.csv"
  else:
    filename = "C:\\Users\\adlogan\\Dropbox\\Projects\\Frequency Conversion\\Layout\\KLayout\\Inverse Design\\GaPOx200_shg2_2021_04_14.csv"
    if thickness != 200:
        warning("Resonator version not found: " + str(thickness))
  #pixel = pya.Shape()
  pixel = pya.Polygon(pya.Box(0,0,size_px_x+abs(enlarge),size_px_y+abs(enlarge)))
  
  
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    rownum = 0
    pixels = set()
    #pixels = layout.create_cell('pixels')
    all_pixels = set()
  
    for row in reader:
      #print(row)
      rownum += 1
      length = len(row)
      for colnum in range(len(row)):
        tf = pya.Trans(pya.Point(colnum*size_px_x, -rownum*size_px_y))
        all_pixels.add(tf.trans(pixel))
        #print(float(row[colnum]))
        if (negative ^ (float(row[colnum])!=1)):
          #pixels.shapes(layer).insert(tf.trans(pixel))
          pixels.add(tf.trans(pixel))
        
  
  pr = pya.EdgeProcessor()
  
  #print(length)
  #print(length*size_px_x/scale)
    
  full_shape = pr.boolean_p2p(list(pixels),list(pixels),pya.EdgeProcessor.ModeOr,False,True)
  
  if negative:
    holes = full_shape
    region = pr.boolean_p2p(list(all_pixels),list(all_pixels),pya.EdgeProcessor.ModeOr,False,True)
    full_shape = pr.boolean_p2p(region,holes,pya.EdgeProcessor.ModeANotB,False,True)
    
  
  px_shift =  0#round(abs(enlarge)/2)
  
  v_shift = round(((rownum-1)*size_px_y - abs(enlarge))/2)
  print(v_shift/scale)
  h_shift = 12400*scale  + abs(enlarge)
  rad = (90+angle)*math.pi/180
   
  trans_center = pya.Trans(0, v_shift)
  trans_45 = pya.ICplxTrans(1,90+angle,False,0,0)
  
  trans_end = pya.Trans(round(h_shift*math.cos(rad)-0*math.sin(rad)), round(0*math.cos(rad)+h_shift*math.sin(rad)))
  
  print(trans_end)
  
  if diagonal:
    trans_center = trans_45*trans_center
  
  shapes = set()
  for s in full_shape:
    #shapes.add(s)
    shapes.add(trans_center*s)
  
  return (shapes, trans_end);