import pya
import math
import photonics as p
import label as L
import GaP_SiN_125_constants as c
import DFG_250_structures as s

from importlib import reload
reload(s)
reload(c)
reload(p)
reload(L)

path = 'C:/Users/adlogan/Dropbox/Frequency Conversion/Data/KLayout/GaP_SiN/2019_06_26 Igor Chip/'
path_test = path + 'Devices/'
path_array = path + 'Arrays/'

filename_full = 'Igor_v1'

layout = pya.Layout()
origin = pya.Point(0,0)

layout.dbu = 0.001/c.scale
GaP = layout.layer(1,0)

ring_mod = {'r420':list(zip(range(-40,-20),range(-20,0),range(0,20),range(20,40)))}

top = layout.create_cell("top")

marker = layout.create_cell("marker")

for shape in p.marker(origin, c.scale, c.res)[0]:
	marker.shapes(GaP).insert(shape)

digits = L.label_gen(c.text_spec['h'], c.text_spec['t'], c.text_spec['res'])

digit_cells = {}

for handle in digits:
  digit_cells[handle] = layout.create_cell(handle)
  for shape in digits[handle]:
    digit_cells[handle].shapes(GaP).insert(shape)
	

grating_cells = {}

for lambda_type in ['600TE']:
	grating_cells[lambda_type] = {}
	for shape_type in c.gr_spec[lambda_type]['shape']:
		filename = 'grating_' + lambda_type + '_' + shape_type
		gr_path = [lambda_type]
		gr_shape_path = [shape_type]
		if lambda_type in c.wg_spec:
			wg_path = [lambda_type]
		else:
			wg_path = ['Multi']
		
		grating = s.gr_from_spec(origin,wg_path,gr_path,gr_shape_path)
		
		grating_cells[lambda_type][shape_type] = layout.create_cell(filename)
		
		for shape in grating[0]:
			grating_cells[lambda_type][shape_type].shapes(GaP).insert(shape)
		
		grating_cells[lambda_type][shape_type].write(path_test + filename + '.gds')



multi_ring_cells = {}
multi_ring_cell_pts = {}

for ring_type in ring_mod:
	multi_ring_cells[ring_type] = {}
	multi_ring_cell_pts[ring_type] = {}
	ring_path = ['disc',ring_type]
	wg_path = ['600TE']
	layout_path = ['multi_ring','disc',ring_type]
	for cp_type in c.ring_spec['disc'][ring_type]['cp']['600TE']:
		multi_ring_cells[ring_type][cp_type] = {}
		multi_ring_cell_pts[ring_type][cp_type] = {}
		ring_cp_paths = [['600TE',cp_type]]
		for mod_type in ring_mod[ring_type]:
			filename = 'multidisc_' + ring_type + '_c' + cp_type + '_mod' + str(mod_type[2])
			multi_ring_cells[ring_type][cp_type][mod_type] = layout.create_cell(filename)
			
			current_cell = multi_ring_cells[ring_type][cp_type][mod_type]
			
			r_mods = [{'r':mod} for mod in mod_type]
			
			(shapes,pt_in,pt_out,pt_marker,pt_label) = s.multi_coupled_ring_from_spec(origin, ring_path, r_mods, ring_cp_paths, wg_path, layout_path)
			
			for shape in shapes:
				current_cell.shapes(GaP).insert(shape)
			
			
			current_cell.insert(pya.CellInstArray(marker.cell_index(), pya.Trans(pt_marker[1],False,pt_marker[0].x,pt_marker[0].y)))
			
			current_cell.insert(pya.CellInstArray(grating_cells['600TE']['ell'].cell_index(), pya.Trans(pt_in[1],False,pt_in[0].x,pt_in[0].y)))
			current_cell.insert(pya.CellInstArray(grating_cells['600TE']['ell'].cell_index(), pya.Trans(pt_out[1],False,pt_out[0].x,pt_out[0].y)))
			
			multi_ring_cell_pts[ring_type][cp_type][mod_type] = pt_label[0]
			
			current_cell.write(path_test + filename + '.gds')



gtest_cells = {}
gtest_cell_pts = {}

for lambda_type in grating_cells:
	if lambda_type not in gtest_cells:
		gtest_cells[lambda_type] = {}
		gtest_cell_pts[lambda_type] = {}
	
	
	if lambda_type in c.wg_spec:
		wg_path = [lambda_type]
	else:
		wg_path = ['Multi']
	
	gr_path = [lambda_type]
	layout_path = ['gtest',lambda_type]
	
	for shape_type in ['ell']:
		filename = 'gtest_' + lambda_type + '_' + shape_type
		gr_shape_path = [shape_type]
		
		gtest_cells[lambda_type][shape_type] = layout.create_cell(filename)
		
		current_cell = gtest_cells[lambda_type][shape_type]
		
		(gtest_shapes, pt_gr_in, pt_gr_out, pt_label) = s.gtest_from_spec(origin, wg_path, gr_path, gr_shape_path, layout_path, 2)

		for shape in gtest_shapes:
			current_cell.shapes(GaP).insert(shape)

		current_cell.insert(pya.CellInstArray(grating_cells[lambda_type][shape_type].cell_index(), pya.Trans(pt_gr_in[1],False,pt_gr_in[0].x,pt_gr_in[0].y)))
		current_cell.insert(pya.CellInstArray(grating_cells[lambda_type][shape_type].cell_index(), pya.Trans(pt_gr_out[1],False,pt_gr_out[0].x,pt_gr_out[0].y)))
		
		gtest_cell_pts[lambda_type][shape_type] = pt_label[0]
				
		current_cell.write(path_test + filename + '.gds')
			



multi_ring_array_cells = {}
cp_label = {'20K':'0', '50K':'1', '100K':'2','200K':'3'}

for ring_type in multi_ring_cells:
	multi_ring_array_cells[ring_type] = {}
	
	for cp_type in multi_ring_cells[ring_type]:
		filename = 'array_multi_ring_' + ring_type + '_cp' + cp_type
		multi_ring_array_cells[ring_type][cp_type] = layout.create_cell(filename)
		
		current_array = multi_ring_array_cells[ring_type][cp_type]
		x_num = c.array_spec['multi_ring']['disc'][ring_type]['x_num']
		
		for dy in range(math.ceil(len(multi_ring_cells[ring_type][cp_type])/x_num)):
			for dx in range(x_num):
				array_trans = pya.Trans(0,False,dx*c.array_spec['multi_ring']['disc'][ring_type]['x'][0],dy*c.array_spec['multi_ring']['disc'][ring_type]['y'][1])
				
				mod_type = ring_mod[ring_type][dx + dy*x_num]
				
				current_array.insert(pya.CellInstArray(multi_ring_cells[ring_type][cp_type][mod_type].cell_index(), array_trans))
				
				label = cp_label[cp_type] + str(dy) + str(dx)
				
				L.label_insert(current_array, digit_cells, c.text_spec['d'], label, array_trans.trans(multi_ring_cell_pts[ring_type][cp_type][mod_type]))
		
		current_array.write(path_array + filename + '.gds')
		top.insert(pya.CellInstArray(current_array.cell_index(), pya.Trans()))	


gtest_array_cells = {}

for gr_type in gtest_cells:
	spec = c.array_spec['gtest'][gr_type]
	gtest_array_cells[gr_type] = {}
	
	shape_types = ['ell']
	
	for shape_type in shape_types:
		filename = 'array_gtest_' + gr_type + '_' + shape_type
		
		gtest_array_cells[gr_type][shape_type] = layout.create_cell(filename)
		current_cell = gtest_array_cells[gr_type][shape_type]
		
		gtest = gtest_cells[gr_type][shape_type]
		
		L.label_insert(current_cell, digit_cells, c.text_spec['d'], c.gr_spec[gr_type]['label'], gtest_cell_pts[gr_type][shape_type])
		
		for dx in range(spec['rep']):
			current_cell.insert(pya.CellInstArray(gtest.cell_index(), pya.Trans(0,False,dx*spec['x'][0],dx*spec['x'][1])))
		
		top.insert(pya.CellInstArray(current_cell.cell_index(), pya.Trans()))
		current_cell.write(path_array + filename + '.gds')
		
	

top.write(path + filename_full + '.gds')