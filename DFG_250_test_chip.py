import pya
import math
import photonics as p
import label as L
import DFG_250_constants as c
import DFG_250_structures as s

from importlib import reload
reload(s)
reload(c)
reload(p)
reload(L)

path = 'C:/Users/adlogan/Dropbox/Frequency Conversion/Data/KLayout/DFG250/2019 01 08 Structures/'
path_test = path + 'Devices/'
path_array = path + 'Arrays/'

filename_full = 'DFG250_Test_1'

layout = pya.Layout()
origin = pya.Point(0,0)

layout.dbu = 0.001/c.scale
GaP = layout.layer(1,0)

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

for lambda_type in c.gr_spec:
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


lr_cells = {}
lr_cell_pts = {}

for lambda_type in c.ring_spec:
	if lambda_type not in lr_cells:
		lr_cells[lambda_type] = {}
		lr_cell_pts[lambda_type] = {}
		
	if lambda_type in c.wg_spec:	#Single WL loss rings
		wg_path = [lambda_type]
		gr_path = [lambda_type]
		gr_shape_path = ['ell']
		
		layout_path = ['lr',lambda_type]
		
		for ring_type in c.ring_spec[lambda_type]:
			if ring_type not in lr_cells[lambda_type]:
				lr_cells[lambda_type][ring_type] = {}
				lr_cell_pts[lambda_type][ring_type] = {}
			ring_path = [lambda_type,ring_type]
			for couple_type in c.ring_spec[lambda_type][ring_type]['cp']:
				filename = 'lr_' + lambda_type + '_' + ring_type + '_c' + couple_type
				ring_cp_path = [couple_type]
			
				lr_cells[lambda_type][ring_type][couple_type] = layout.create_cell(filename)
				
				current_cell = lr_cells[lambda_type][ring_type][couple_type]
				
				
				(lr_shapes, pt_gr_in, pt_gr_trans, pt_gr_drop, pt_label_1, pt_label_2, pt_marker) = s.lr_from_spec(origin, wg_path, ring_path, ring_cp_path, gr_path, gr_shape_path, layout_path)
				
				for shape in lr_shapes:
					current_cell.shapes(GaP).insert(shape)
				
				current_cell.insert(pya.CellInstArray(grating_cells[lambda_type]['ell'].cell_index(), pya.Trans(pt_gr_in[1],False,pt_gr_in[0].x,pt_gr_in[0].y)))
				current_cell.insert(pya.CellInstArray(grating_cells[lambda_type]['ell'].cell_index(), pya.Trans(pt_gr_drop[1],False,pt_gr_drop[0].x,pt_gr_drop[0].y)))
				current_cell.insert(pya.CellInstArray(grating_cells[lambda_type]['ell'].cell_index(), pya.Trans(pt_gr_trans[1],False,pt_gr_trans[0].x,pt_gr_trans[0].y)))
				current_cell.insert(pya.CellInstArray(marker.cell_index(), pya.Trans(pt_marker[1],False,pt_marker[0].x,pt_marker[0].y)))
				
				L.label_insert(current_cell, digit_cells, c.text_spec['d'], c.ring_spec[lambda_type][ring_type]['cp'][couple_type]['label'], pt_label_1[0])
				
				lr_cell_pts[lambda_type][ring_type][couple_type] = pt_label_2[0]
				
				current_cell.write(path_test + filename + '.gds')
		
		
	elif lambda_type == 'SHG':	#SHG Case
		ring_path = ['SHG','v1']
		
		for wl_type in c.ring_spec['SHG']['v1']['cp']:
			if wl_type not in lr_cells['SHG']:
				lr_cells['SHG'][wl_type] = {}
				lr_cell_pts['SHG'][wl_type] = {}
			gr_path = [wl_type]
			wg_path = [wl_type]
			gr_shape_path = ['ell']
			layout_path = ['lr','SHG','v1',wl_type]
			
			for couple_type in c.ring_spec['SHG']['v1']['cp'][wl_type]:
				filename = 'lr_SHGv1_' + wl_type + '_c' + couple_type
				ring_cp_path = [wl_type,couple_type]
				
				lr_cells['SHG'][wl_type][couple_type] = layout.create_cell(filename)
				
				current_cell = lr_cells['SHG'][wl_type][couple_type]
				
				(lr_shapes, pt_gr_in, pt_gr_trans, pt_gr_drop, pt_label_1, pt_label_2, pt_marker) = s.lr_from_spec(origin, wg_path, ring_path, ring_cp_path, gr_path, gr_shape_path, layout_path)
				
				for shape in lr_shapes:
					current_cell.shapes(GaP).insert(shape)
				
				current_cell.insert(pya.CellInstArray(grating_cells[wl_type]['ell'].cell_index(), pya.Trans(pt_gr_in[1],False,pt_gr_in[0].x,pt_gr_in[0].y)))
				current_cell.insert(pya.CellInstArray(grating_cells[wl_type]['ell'].cell_index(), pya.Trans(pt_gr_drop[1],False,pt_gr_drop[0].x,pt_gr_drop[0].y)))
				current_cell.insert(pya.CellInstArray(grating_cells[wl_type]['ell'].cell_index(), pya.Trans(pt_gr_trans[1],False,pt_gr_trans[0].x,pt_gr_trans[0].y)))
				current_cell.insert(pya.CellInstArray(marker.cell_index(), pya.Trans(pt_marker[1],False,pt_marker[0].x,pt_marker[0].y)))
				
				L.label_insert(current_cell, digit_cells, c.text_spec['d'], c.ring_spec['SHG']['v1']['cp'][wl_type][couple_type]['label'], pt_label_1[0])
				
				lr_cell_pts['SHG'][wl_type][couple_type] = pt_label_2[0]
				
				current_cell.write(path_test + filename + '.gds')
	

gtest_cells = {}
gtest_cell_pts = {}

for lambda_type in c.gr_spec:
	if lambda_type not in gtest_cells:
		gtest_cells[lambda_type] = {}
		gtest_cell_pts[lambda_type] = {}
	
	if lambda_type in c.wg_spec:
		wg_path = [lambda_type]
	else:
		wg_path = ['Multi']
	
	gr_path = [lambda_type]
	layout_path = ['gtest',lambda_type]
	
	for shape_type in c.gr_spec[lambda_type]['shape']:
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
		
	
	
	filename = 'gtest_' + lambda_type + '_hyb'
	gr_shape_path = ['ell']
		
	gtest_cells[lambda_type]['hyb'] = layout.create_cell(filename)
		
	current_cell = gtest_cells[lambda_type]['hyb']
		
	(gtest_shapes, pt_gr_in, pt_gr_out, pt_label) = s.gtest_from_spec(origin, wg_path, gr_path, gr_shape_path, layout_path, 2)

	for shape in gtest_shapes:
		current_cell.shapes(GaP).insert(shape)

	current_cell.insert(pya.CellInstArray(grating_cells[lambda_type]['str'].cell_index(), pya.Trans(pt_gr_in[1],False,pt_gr_in[0].x,pt_gr_in[0].y)))
	current_cell.insert(pya.CellInstArray(grating_cells[lambda_type]['ell'].cell_index(), pya.Trans(pt_gr_out[1],False,pt_gr_out[0].x,pt_gr_out[0].y)))
		
	gtest_cell_pts[lambda_type]['hyb'] = pt_label[0]
				
	current_cell.write(path_test + filename + '.gds')	



lr_array_cells = {}

for ring_type in lr_cells:
	if ring_type == 'SHG':
		lr_array_cells[ring_type] = {}
		for lambda_type in lr_cells[ring_type]:
			filename = 'array_lr_SHGv1_' + lambda_type
			
			lr_array_cells[ring_type][lambda_type] = layout.create_cell(filename)
			
			current_cell = lr_array_cells[ring_type][lambda_type]
			
			couple_type = list(lr_cells[ring_type][lambda_type].keys())
			
			couple_type.sort(reverse = True)
			
			spec = c.array_spec['lr'][ring_type]['v1'][lambda_type]
			
			
			
			for dx in range(len(couple_type)):
			
				lr = lr_cells[ring_type][lambda_type][couple_type[dx]]
				pt = lr_cell_pts[ring_type][lambda_type][couple_type[dx]]
				
				for dy in range(spec['rep']):
					transform = pya.Trans(0,False,dx*spec['x'],dy*spec['y'])
					
					L.label_insert(current_cell, digit_cells, c.text_spec['d'], str(dy) + str(dx), transform.trans(pt))
					
					current_cell.insert(pya.CellInstArray(lr.cell_index(), transform))
			
			current_cell.write(path_array + filename + '.gds')
			top.insert(pya.CellInstArray(current_cell.cell_index(), pya.Trans()))
	else:
		filename = 'array_lr_' + ring_type
		lr_array_cells[ring_type] = layout.create_cell(filename)
		
		current_cell = lr_array_cells[ring_type]
		
		spec = c.array_spec['lr'][ring_type]
		
		dx = 0
		
		widths = list(lr_cells[ring_type].keys())
		widths.sort()
		
		for width_type in widths:
			couples = list(lr_cells[ring_type][width_type].keys())
			couples.sort(reverse = True)
			for couple_type in couples:
			
				lr = lr_cells[ring_type][width_type][couple_type]
				pt = lr_cell_pts[ring_type][width_type][couple_type]
					
				for dy in range(spec['rep']):
					transform = pya.Trans(0,False,dx*spec['x'],dy*spec['y'])
					
					L.label_insert(current_cell, digit_cells, c.text_spec['d'], str(dy) + str(dx), transform.trans(pt))
					
					current_cell.insert(pya.CellInstArray(lr.cell_index(), transform))
				dx += 1
		
		current_cell.write(path_array + filename + '.gds')
		top.insert(pya.CellInstArray(current_cell.cell_index(), pya.Trans()))
		

gtest_array_cells = {}
gtest_full_arrays = {}

for gr_type in gtest_cells:
	spec = c.array_spec['gtest'][gr_type]
	filename_array = 'array_gtest_full_' + gr_type
	gtest_array_cells[gr_type] = {}
	gtest_full_arrays[gr_type] = layout.create_cell(filename_array)
	
	current_array = gtest_full_arrays[gr_type]
	
	dx = 0
	
	shape_types = list(gtest_cells[gr_type].keys())
	shape_types.sort()
	
	for shape_type in shape_types:
		filename = 'array_gtest_' + gr_type + '_' + shape_type
		
		gtest_array_cells[gr_type][shape_type] = layout.create_cell(filename)
		current_cell = gtest_array_cells[gr_type][shape_type]
		
		gtest = gtest_cells[gr_type][shape_type]
		
		L.label_insert(current_cell, digit_cells, c.text_spec['d'], c.gr_spec[gr_type]['label'], gtest_cell_pts[gr_type][shape_type])
		
		for dy in range(spec['rep']):
			current_cell.insert(pya.CellInstArray(gtest.cell_index(), pya.Trans(0,False,dy*spec['x'],dy*spec['y'])))
		
		current_cell.write(path_array + filename + '.gds')
		
		
		current_array.insert(pya.CellInstArray(current_cell.cell_index(), pya.Trans(0,False,dx*spec['x_full'],dx*spec['y_full'])))
		
		dx += 1
		
		
	top.insert(pya.CellInstArray(current_array.cell_index(), pya.Trans()))
	current_array.write(path_array + filename_array + '.gds')
	
	
	

top.write(path + filename_full + '.gds')