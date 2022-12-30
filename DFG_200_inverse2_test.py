import pya
import math
import layout_from_csv_fn as inv


from importlib import reload
reload(inv)

path = 'C:\\Users\\adlogan\\Dropbox\\Projects\\Frequency Conversion\\Layout\\KLayout\\Inverse Design\\'

layout = pya.Layout()
origin = pya.Point(0,0)

scale = 20

layout.dbu = 0.001/scale
GaP = layout.layer(1,0)

enlarge = range(-15,6)

for x in enlarge:
  cell = layout.create_cell("x"+str(x))
  
  shapes = inv.inverse_design_v2(0, 0, 0, x*scale, scale)
  
  for shape in shapes:
    cell.shapes(GaP).insert(shape)
  
  cell.write(path + 'Test Structures\\res_v2_x' + str(x) + '_L0.gds')