import pya
import math
import DFG2_constants as c

def total_area(cell,layer):
  area = 0
  cell.flatten(0)
  for shape in cell.shapes(layer).each():
    area = area + shape.area()
    
  return area
  


layout = pya.Layout()
layout.dbu = 0.001/c.scale
GaP = layout.layer(1,0)

layout.read("C:\\Users\\Alan\\Desktop\\OptoSpin Projects\\KLayout\\DFG2 Structures\\DFG_test_v2.gds")

top = layout.cell("pattern")

a = total_area(top,GaP)

print(a*(layout.dbu**2))

layout.write("C:\\Users\\Alan\\Desktop\\OptoSpin Projects\\KLayout\\DFG2 Structures\\DFG_test_flat.gds")