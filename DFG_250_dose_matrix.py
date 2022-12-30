import pya
import math
import photonics as p
import DFG_250_constants as c
import label

from importlib import reload
# reload(c)
reload(p)
# reload(L)

path = 'C:\\Users\\adlogan\\Dropbox\\Frequency Conversion\\Data\\KLayout\\2018_12_04 Dose Matrix\\'

layout = pya.Layout()
layout.dbu = 0.001/c.scale
GaP = layout.layer(1,0)

top = layout.create_cell('top')
origin = pya.Point(0,0)


# create cells for labels
# char_shapes = label.label_gen(c.text_h, c.text_t, c.text_res)
# char_cells = {}
# for handle in char_shapes:
  # char_cells[handle] = layout.create_cell(handle)
  # for shape in char_shapes[handle]:
    # char_cells[handle].shapes(GaP).insert(shape)

# Create a cell containing a concentric-circle marker (usually used for microscope image feedback, automated measurement)
marker = layout.create_cell('marker')
for shape in p.marker(origin,c.scale,c.res)[0]:
  marker.shapes(GaP).insert(shape)

marker.write(path + "marker.gds")

top.insert(pya.CellInstArray(marker.cell_index(),pya.Trans()))
# Create a cell containing a centered 50nm circle


# array_1 = layout.create_cell("array_50")
# period_1 = 200*c.scale;
# rep_1 = 18;
# vector_h1 = pya.Vector(period_1,0);
# vector_v1 = pya.Vector(0,period_1);
# trans_1 = pya.Trans(pya.Point(-1*period_1*rep_1/2,-1*period_1*rep_1/2))

# array_1.insert(pya.CellInstArray(circle.cell_index(),trans_1,vector_h1,vector_v1,rep_1,rep_1))


# array_1.write(path + 'array_dense.gds')

w_wg = [50,100,250]

L_wg = [4,1,2,1,3,1,2,1,4]

rep_1 = 19
rep_2 = 7

for w in w_wg:
	line_array_name = "array_line_" + str(w)
	width = w *c.scale
	line_array = layout.create_cell(line_array_name)
	
	current_start = pya.Point(0,0)
	line_trans = pya.Trans(0,width + 50*c.scale)

	for span in L_wg + L_wg[::-1]:
		shapes = p.waveguide(current_start, 270, width, width*20*span)[0]
		for shape in shapes:
			line_array.shapes(GaP).insert(shape)
		
		current_start = line_trans.trans(current_start)
	
	line_array.write(path + line_array_name + '.gds')
	
	
	circle = layout.create_cell("circle" + str(w))
	for shape in p.circle(origin,round(width/2),c.res)[0]:
		circle.shapes(GaP).insert(shape)
	
	array_1_name = "array_dense_" + str(w)
	array_2_name = "array_sparse_" + str(w)
	
	array_1 = layout.create_cell(array_1_name)
	array_2 = layout.create_cell(array_2_name)
	
	vector_h1 = pya.Vector(width + 50*c.scale,0)
	vector_v1 = pya.Vector(0, width + 50*c.scale)
	
	vector_h2 = pya.Vector((width + 50*c.scale)*3,0)
	vector_v2 = pya.Vector(0, (width + 50*c.scale)*3)
	
	array_1.insert(pya.CellInstArray(circle.cell_index(),pya.Trans(),vector_h1,vector_v1,rep_1,rep_1))
	array_2.insert(pya.CellInstArray(circle.cell_index(),pya.Trans(),vector_h2,vector_v2,rep_2,rep_2))
	
	array_1.write(path + array_1_name + '.gds')
	array_2.write(path + array_2_name + '.gds')
	
	top.insert(pya.CellInstArray(line_array.cell_index(),pya.Trans()))
	top.insert(pya.CellInstArray(array_1.cell_index(),pya.Trans()))
	top.insert(pya.CellInstArray(array_2.cell_index(),pya.Trans()))
	
top.write(path + "dose_matrix.gds")


